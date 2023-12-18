import os
API_PATH = os.path.join(os.getcwd(), "app")

import sys
sys.path.insert(1, os.getcwd())
sys.path.insert(1, API_PATH)

try:
    import app.SpaceTradersAPI as SpaceTradersAPI
except:
    import SpaceTradersAPI as SpaceTradersAPI

from Config import TOKEN
from icecream import ic as print
import json
import time

EXPORT_GALAXY_PATH = os.path.join("data", "galaxys.json")

if __name__ == "__main__":
    # Create a new instance of the SpaceTraders class
    api = SpaceTradersAPI.SpaceTraders(TOKEN)

    # Initialize parameters
    systems_count = 1 # Set to 1 to start the loop
    page = 1          # Start at page 1
    all_systems = []  # List to store all the systems
    max_pages = 0     # Max pages to loop through

    # Loop through all the pages till we get no more systems
    while systems_count > 0:
        # Get the systems for the current page
        results = api.get_systems(page=page, limit=20)

        # Get the systems from the results
        systems = results["data"]

        # Add the systems to the list of all systems
        all_systems.extend(systems)

        # Get the meta data from the results to print some info
        meta = results["meta"]
        total_records = meta["total"]
        max_pages = total_records // 20
        print(f"Page {page} of {max_pages} ({total_records} total records)")

        # Count the number of systems we got and increment the page for the next loop
        systems_count = len(systems)
        page += 1

        # Sleep for 1 second to avoid rate limiting
        time.sleep(1)
        break

    # Write the systems to a file
    with open(EXPORT_GALAXY_PATH, "w") as f:
        f.write(json.dumps(all_systems, indent=4))