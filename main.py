from flask import Flask, render_template
from flask_socketio import SocketIO, send
import app.Model as Model
from icecream import ic as print

app = Flask(
    __name__,
    static_folder = "app/static",
    template_folder = "app/templates"
)
app.config["SECRET_KEY"] = ""
socketio = SocketIO(app)

@app.route("/")
def index():
    response = Model.get_agent()
    print(response)
    return render_template("index.html", agent=response)

@app.route("/waypoints")
def waypoints():
    response = Model.get_agent()
    print(response)
    systems = Model.get_systems()
    return render_template("waypoints.html", agent=response, systems=systems)

@socketio.on("get_contracts")
def get_contracts_handler():
    available_contracts = Model.get_contracts()
    print(available_contracts)
    return available_contracts

@socketio.on("accept_contract")
def accept_contracts_handler(contract_id: str):
    accepted_contract = Model.accept_contract(contract_id)
    print(accepted_contract)
    return accepted_contract

@socketio.on("get_galaxy_data")
def galaxy_handler():
    galaxy = Model.get_galaxy_data()

    return galaxy

@socketio.on("get_waypoints")
def get_waypoints(trait: str, system: str):
    waypoints = Model.get_waypoints(
        trait=trait,
        system=system
    )

    print(waypoints)

    return waypoints

if __name__ == "__main__":
    Model.init()
    app.run(host="0.0.0.0")