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
    return render_template("index.html", agent=Model.login())

@socketio.on("get_contracts")
def contracts_handler():
    available = Model.get_contracts()

    return available

@socketio.on("get_galaxy_data")
def galaxy_handler():
    galaxy = Model.get_galaxy_data()

    return galaxy

if __name__ == "__main__":
    Model.init()
    app.run()