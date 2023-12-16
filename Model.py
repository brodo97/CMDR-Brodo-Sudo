import app.SpaceTradersAPI as SpaceTradersAPI
from Config import *
import os


API = SpaceTradersAPI.SpaceTraders(TOKEN)

clear = lambda: os.system("cls" if os.name == "nt" else "clear")


def login() -> None:
    """ Logs into the SpaceTraders API and prints the initial data
    """
    
    print("Logging in...\n")

    result = API.get_my_agent()
    result = result["data"]

    clear()

    print("Login successful, welcome back {YOUR_NAME}!")
    print("Here is your agent data:")

    for key, value in result.items():
        print(f" - {key.title()}: {value}")
    
    