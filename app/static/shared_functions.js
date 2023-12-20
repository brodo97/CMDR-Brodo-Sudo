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
      var units = contract.terms.deliver[j].unitsRequired;
      var trade_symbol = contract.terms.deliver[j].tradeSymbol;
      var trade_dest = contract.terms.deliver[j].destinationSymbol;
      actions += `${units}x ${trade_symbol} on ${trade_dest}<br>`;
    }

    // Calculate ETAs
    var expire_at = moment(contract.deadlineToAccept);
    var deadline = moment(contract.terms.deadline)
    var eta_expire = expire_at.fromNow();
    var eta_deadline = deadline.fromNow();

    var table_row = "";

    if (table_id === "#av_contracts"){
      table_row = `
        <tr>
          <td class='left aligned'>${contract.factionSymbol}</td>
          <td>${contract.type}</td>
          <td>${eta_expire}</td>
          <td>${eta_deadline}</td>
          <td>${actions}</td>
          <td><i class="bi bi-currency-dollar"></i>${numberWithCommas(contract.terms.payment.onAccepted)}</td>
          <td><i class="bi bi-currency-dollar"></i>${numberWithCommas(contract.terms.payment.onFulfilled)}</td>
          <td><button type="button" class="btn btn-success" onclick='accept_contract("${contract.id}")'>Accept</button></td>
        </tr>
      `;
    }else{
      table_row = `
        <tr>
          <td class='left aligned'>${contract.factionSymbol}</td>
          <td>${contract.type}</td>
          <td>${eta_deadline}</td>
          <td>${actions}</td>
          <td><i class="bi bi-currency-dollar"></i>${numberWithCommas(contract.terms.payment.onFulfilled)}</td>
        </tr>
      `;
    }

    // Append to table
    $(table_id).append(
      table_row
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
    console.log(response);
    fill_contract_table(response);
  });
}

function accept_contract(contract_id){
  socket.emit("accept_contract", contract_id, (response) => {
    console.log(response);
    get_contracts();
  });
}

function get_waypoints(){
  var trait = $("#trait").val();
  var system = $("#system").val();

  // Check if parameters are empty
  if (trait === "" || system === ""){
    $("#search_waypoint_card").append(`
    <div class="alert alert-warning alert-dismissible fade show" role="alert">
      <strong>Warning!</strong> You must enter a trait and system.
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    `);
    return;
  }

  socket.emit("get_waypoints", trait, system, (waypoints) => {
    console.log(waypoints);
  });
}