import app.SpaceTradersAPI as SpaceTradersAPI
from Config import *
import json

API = None
GALAXY_DATA = None
CONTRACTS = None

def init() -> None:
    """Initializes the API."""

    global API

    API = SpaceTradersAPI.SpaceTraders(TOKEN)

def login() -> dict:
    """Logs into SpaceTraders and returns the response."""

    global API

    result = API.get_my_agent()

    return result["data"]

def get_contracts() -> dict:
    """Gets the contracts from SpaceTraders and returns the response."""

    global API, CONTRACTS

    # Return the cached data if it exists
    if CONTRACTS is not None:
        return CONTRACTS

    result = API.get_contracts()

    return result["data"]

def get_galaxy_data() -> dict:
    """Gets the galaxy data from SpaceTraders and returns the response."""

    global GALAXY_DATA

    # Return the cached data if it exists
    if GALAXY_DATA is not None:
        return GALAXY_DATA

    with open("data/galaxy.json", "r") as f:
        result = json.loads(f.read())

    data = dict()
    
    data.update({
        "system_count": len(result),
        "star_by_type": dict()
    })

    for system in result:
        data["star_by_type"].update({
            system["type"]: data["star_by_type"].get(system["type"], 0) + 1
        })

    return data