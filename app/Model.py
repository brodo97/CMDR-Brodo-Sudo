import app.SpaceTradersAPI as SpaceTradersAPI
from Config import *
import json
import time

API = None
AGENT = None
GALAXY_DATA = None
CONTRACTS = None
WAYPOINTS = dict()

def init() -> None:
    """Initializes the API."""

    global API

    API = SpaceTradersAPI.SpaceTraders(TOKEN)

def get_agent() -> dict:
    """Logs into SpaceTraders and returns the response."""

    global API, AGENT

    # Check if the agent has already been cached
    if AGENT is not None:
        # Check if the agent is relatively new
        if time.time() - AGENT[1] < 120:
            return AGENT[0]

    result = API.get_my_agent()

    AGENT = (result["data"], time.time())

    return AGENT[0]

def get_contracts(force_update: bool = False) -> dict:
    """ Gets the contracts from SpaceTraders and returns the response.
    
    Args:
        force_update (bool): Forces the contracts to be updated
    
    Returns:
        dict: Response from SpaceTraders
    """

    global API, CONTRACTS

    # Check if the contracts have already been cached
    if CONTRACTS is not None and not force_update:
        # Check if the contracts are relatively new
        if time.time() - CONTRACTS[1] < 120:
            return CONTRACTS[0]

    result = API.get_contracts()

    CONTRACTS = (result["data"], time.time())

    return CONTRACTS[0]

def accept_contract(contract_id: str) -> dict:
    """ Accepts a contract and returns the response.

    Args:
        contract_id (str): ID of the contract to accept

    Returns:
        dict: Response from SpaceTraders
    """

    global API

    result = API.accept_contract(contract_id)

    get_contracts(force_update=True)

    return result


def load_galaxy_data() -> None:
    """Loads the galaxy data from SpaceTraders and saves it to a file."""

    global GALAXY_DATA

    # Return the cached data if it exists
    if GALAXY_DATA is None:
        with open("data/galaxy.json", "r") as f:
            GALAXY_DATA = json.loads(f.read())


def get_galaxy_data() -> dict:
    """Gets the galaxy data from SpaceTraders and returns the response."""

    global GALAXY_DATA

    # Return the cached data if it exists
    load_galaxy_data()

    data = dict()
    
    data.update({
        "system_count": len(GALAXY_DATA),
        "star_by_type": dict()
    })

    for system in GALAXY_DATA:
        data["star_by_type"].update({
            system["type"]: data["star_by_type"].get(system["type"], 0) + 1
        })

    return data

def get_systems() -> list:
    """ Gets the galaxy data from SpaceTraders and returns the response.

    Returns:
        list: List of systems

    """

    global GALAXY_DATA

    # Return the cached data if it exists
    load_galaxy_data()

    data = list()
    
    for system in sorted(GALAXY_DATA, key=lambda x: x["symbol"]):
        data.append(system["symbol"])

    return data

def get_waypoints(trait: str, system: str) -> dict:
    """ Gets the waypoints from SpaceTraders and returns the response.

    Args:
        trait (str): The trait to filter by
        system (str): The system to filter by

    Returns:
        dict: Response from SpaceTraders
    """

    global API, WAYPOINTS

    # Check if the waypoints have already been cached
    if system in WAYPOINTS:
        return WAYPOINTS[system]

    result = API.get_system_waypoints(
        systemSymbol=system,
        traits=trait
    )

    WAYPOINTS.update({
        system: result["data"]
    })

    return result["data"]