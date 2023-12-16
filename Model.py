import app.SpaceTradersAPI as SpaceTradersAPI
from Config import *
import os
from datetime import datetime

API = SpaceTradersAPI.SpaceTraders(TOKEN)

clear = lambda: os.system("cls" if os.name == "nt" else "clear")


def convert_date(date: str) -> str:
    """ Converts a date from the SpaceTraders API to a more readable format

    Args:
        date (str): The date from the SpaceTraders API

    Returns:
        str: The converted date in: dd/mm/yyyy, hh:mm:ss
    """

    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y, %H:%M:%S")

def convert_in_time_left(date: str) -> str:
    """ How much time is left until date

    Args:
        date (str): The date from the SpaceTraders API

    Returns:
        str: The time left until date
    """

    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    now = datetime.utcnow()

    return str(date - now)
    

def print_contracts(contracts: dict) -> None:
    """ Prints a contracts in a nice format
    """

    print("\nContracts:")

    for contract in contracts["data"]:
        print("Faction: " + contract["factionSymbol"])
        print("Type: " + contract["type"])

        term = contract["terms"]
        payment = term["payment"]
        deliver = term["deliver"]

        print(f"Terms:")

        if contract["accepted"] is True:
            print(f" - Deadline: {convert_date(term['deadline'])} (in {convert_in_time_left(term['deadline'])})")
            print(f" - Payment: {payment['onFulfilled']:,} credits when completed")
        else:
            print(f" - Deadline to accept: {convert_date(contract['deadlineToAccept'])} (in {convert_in_time_left(contract['deadlineToAccept'])})")
            print(f" - Payment: {payment['onAccepted']:,} credits when accepted, {payment['onFulfilled']:,} credits when completed")

        print("Needs:")
        for deliverable in deliver:
            required = deliverable["unitsRequired"]
            fulfilled = deliverable["unitsFulfilled"]
            tradesymbol = deliverable["tradeSymbol"]
            text = f" - {tradesymbol}: "
            if contract["accepted"] is True:
                text += f"Delivered {fulfilled}/{required} units ({100/required*fulfilled:.1f}%). {required - fulfilled} left to go ({100/required*(required-fulfilled):.1f}%)"
            else:
                text += f"{required} units"
            print(text)

        print()

def login() -> None:
    """ Logs into the SpaceTraders API and prints the initial data
    """
    
    print("Logging in...\n")

    result = API.get_my_agent()
    result = result["data"]

    clear()

    print(f"Login successful, welcome back {YOUR_NAME}!")
    print("Here is your agent data:")

    for key, value in result.items():
        print(f" - {key.title()}: {value}")

    contracts = API.get_contracts()    
    print_contracts(contracts)
    

    