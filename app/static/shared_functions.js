// UI elements 
$(".ui.dropdown").dropdown();

// Function to convert a number to a string with commas
function numberWithCommas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// Fill contract tables
function fill_contract_table(contracts){
  var table_id = "";

  // Clear tables
  $("#av_contracts").empty();
  $("#ac_contracts").empty();

  // Fill tables
  for (var i = 0; i < contracts.length; i++){
    var contract = contracts[i];

    // Determine table
    if (contract.accepted === false){
      table_id = "#av_contracts";
    }else{
      table_id = "#ac_contracts";
    }

    console.log(contract, table_id);

    // Cycle through actions (deliveries)
    var actions = "";
    for (var j = 0; j < contract.terms.deliver.length; j++){
      console.log(contract.terms.deliver[j]);
      actions += `${contract.terms.deliver[j].unitsRequired}x ${contract.terms.deliver[j].tradeSymbol} <br>`;
    }

    // Calculate ETAs
    var expire_at = moment(contract.deadlineToAccept);
    var deadline = moment(contract.terms.deadline)
    var eta_expire = expire_at.fromNow();
    var eta_deadline = deadline.fromNow();

    // Append to table
    $(table_id).append(
      "<tr>" +
        "<td class='left aligned'>" + contract.factionSymbol + "</td>" +
        "<td>" + contract.type + "</td>" +
        "<td>" + eta_expire + "</td>" +
        "<td>" + eta_deadline + "</td>" +
        "<td>" + actions + "</td>" +
        "<td><i class='dollar sign icon'></i>" + numberWithCommas(contract.terms.payment.onAccepted) + "</td>" +
        "<td><i class='dollar sign icon'></i>" + numberWithCommas(contract.terms.payment.onFulfilled) + "</td>" +
      "</tr>"
    )

  }
}


// Funcion to process galaxy data
function process_galaxy_data(data){
  var galaxy_description_id = "#galaxy_description";

  // Clear description
  $(galaxy_description_id).empty();

  // Add description
  $(galaxy_description_id).append(
    "<p>There are <b>" + numberWithCommas(data.system_count) + "</b> systems in this galaxy.</p>" +
    "<p>Star by type:</p>" +
    "<ul>"
  )

  // Add star types
  for (var key in data.star_by_type){
    $(galaxy_description_id).append(
      "<li>" + key + ": <b>" + numberWithCommas(data.star_by_type[key]) + "</b></li>"
    )
  }

  // Close list
  $(galaxy_description_id).append(
    "</ul>"
  )
}

var socket = io();
socket.on("connect", function() {
  socket.emit("connected", {data: "I\'m connected!"});
});

function get_contracts(){
  socket.emit("get_contracts", (response) => {
    fill_contract_table(response);
  });
}

window.onload = function() {
  get_contracts();

  socket.emit("get_galaxy_data", (response) => {
    process_galaxy_data(response);
  });
}