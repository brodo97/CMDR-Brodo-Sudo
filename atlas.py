import requests
import json
from rich import print_json as printj
from prettytable import PrettyTable

TOKEN = {}
ENDPOINT = "https://api.spacetraders.io/v2/my/agent"

def main():
    
    with open("token.key", "r") as file:
        TOKEN['Authorization'] = "Bearer "+file.readline()
    try:
        while True:
            console = input(">> ")
            if console == "a":
                view_agent()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user (Ctrl+C).")

def view_agent():
    agent_info = requests.get(ENDPOINT, headers=TOKEN).json()
    printj(data=agent_info)

    # Extract the nested dictionary
    nested_data = agent_info["data"]

    # Create a PrettyTable instance
    table = PrettyTable()

    # Add columns to the table
    table.field_names = ["Key", "Value"]

    # Add rows to the table
    for key, value in nested_data.items():
        table.add_row([key, value])
    # Print the table
    print(table)

if __name__ == "__main__":
    main()