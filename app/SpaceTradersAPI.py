#
# Lib Author: Mattia Brunelli (https://github.com/brodo97)
#
# API Author: Joel Brubaker (joel@spacetraders.io)
#

import requests

class SpaceTraders:
    def __init__(self, token: str) -> None:
        self.token = token  # The token used to authenticate the user
        self.url = 'https://api.spacetraders.io/v2'  # The url of the server

        # The session used to make requests and prepare the session methods for better readability
        self.session = requests.Session()
        self._get = self.session.get
        self._post = self.session.post
        self._patch = self.session.patch
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.token}',
        })

    def get_status(
        self
    ) -> dict:
        '''
        Return the status of the game server.
        This also includes a few global elements, such as announcements, server reset dates and leaderboards.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_agents(
        self,
        page: int = 1,
        limit: int = 10
    ) -> dict:
        '''
        Fetch agents details.

        Args:
            page (int): What entry offset to request. Default: 1
            limit (int): How many entries to return per page. Default: 10

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/agents'

        # Prepare the parameters
        params = dict()

        # Add the parameters to the parameters dict
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit

        # Make the request
        response = self._get(url=url, params=params)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_agent(
        self,
        agentSymbol: str = 'FEBA66'
    ) -> dict:
        '''
        Fetch agent details.

        Args:
            agentSymbol (str): The agent symbol. Default: 'FEBA66'

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/agents/{agentSymbol}'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_factions(
        self,
        page: int = 1,
        limit: int = 10
    ) -> dict:
        '''
        Return a paginated list of all the factions in the game.

        Args:
            page (int): What entry offset to request. Default: 1
            limit (int): How many entries to return per page. Default: 10

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/factions'

        # Prepare the parameters
        params = dict()

        # Add the parameters to the parameters dict
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit

        # Make the request
        response = self._get(url=url, params=params)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_faction(
        self,
        factionSymbol: str
    ) -> dict:
        '''
        View the details of a faction.

        Args:
            factionSymbol (str): The faction symbol

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/factions/{factionSymbol}'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_my_agent(
        self
    ) -> dict:
        '''
        Fetch your agent's details.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/agent'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_contracts(
        self,
        page: int = 1,
        limit: int = 10
    ) -> dict:
        '''
        Return a paginated list of all your contracts.

        Args:
            page (int): What entry offset to request. Default: 1
            limit (int): How many entries to return per page. Default: 10

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/contracts'

        # Prepare the parameters
        params = dict()

        # Add the parameters to the parameters dict
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit

        # Make the request
        response = self._get(url=url, params=params)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_contract(
        self,
        contractId: str
    ) -> dict:
        '''
        Get the details of a contract by ID.

        Args:
            contractId (str): The contract ID

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/contracts/{contractId}'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def accept_contract(
        self,
        contractId: str
    ) -> dict:
        '''
        Accept a contract by ID. 
        
        You can only accept contracts that were offered to you, were not accepted yet, and whose deadlines has not passed yet.

        Args:
            contractId (str): The contract ID to accept.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/contracts/{contractId}/accept'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def deliver_contract(
        self,
        contractId: str
    ) -> dict:
        '''
        Deliver cargo to a contract.
        
        In order to use this API, a ship must be at the delivery location (denoted in the delivery terms as `destinationSymbol` of a contract) and must have a number of units of a good required by this contract in its cargo.
        
        Cargo that was delivered will be removed from the ship's cargo.

        Args:
            contractId (str): The ID of the contract.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/contracts/{contractId}/deliver'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def fulfill_contract(
        self,
        contractId: str
    ) -> dict:
        '''
        Fulfill a contract. Can only be used on contracts that have all of their delivery terms fulfilled.

        Args:
            contractId (str): The ID of the contract to fulfill.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/contracts/{contractId}/fulfill'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_my_ships(
        self,
        page: int = 1,
        limit: int = 10
    ) -> dict:
        '''
        Return a paginated list of all of ships under your agent's ownership.

        Args:
            page (int): What entry offset to request. Default: 1
            limit (int): How many entries to return per page. Default: 10

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships'

        # Prepare the parameters
        params = dict()

        # Add the parameters to the parameters dict
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit

        # Make the request
        response = self._get(url=url, params=params)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def purchase_ship(
        self
    ) -> dict:
        '''
        Purchase a ship from a Shipyard. In order to use this function, a ship under your agent's ownership must be in a waypoint that has the `Shipyard` trait, and the Shipyard must sell the type of the desired ship.
        
        Shipyards typically offer ship types, which are predefined templates of ships that have dedicated roles. A template comes with a preset of an engine, a reactor, and a frame. It may also include a few modules and mounts.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_my_ship(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Retrieve the details of a ship under your agent's ownership.

        Args:
            shipSymbol (str): The symbol of the ship.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_my_ship_cargo(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Retrieve the cargo of a ship under your agent's ownership.

        Args:
            shipSymbol (str): The symbol of the ship.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/cargo'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def create_chart(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Command a ship to chart the waypoint at its current location.
        
        Most waypoints in the universe are uncharted by default. These waypoints have their traits hidden until they have been charted by a ship.
        
        Charting a waypoint will record your agent as the one who created the chart, and all other agents would also be able to see the waypoint's traits.

        Args:
            shipSymbol (str): The symbol of the ship.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/chart'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_ship_cooldown(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Retrieve the details of your ship's reactor cooldown. Some actions such as activating your jump drive, scanning, or extracting resources taxes your reactor and results in a cooldown.
        
        Your ship cannot perform additional actions until your cooldown has expired. The duration of your cooldown is relative to the power consumption of the related modules or mounts for the action taken.
        
        Response returns a 204 status code (no-content) when the ship has no cooldown.

        Args:
            shipSymbol (str): The symbol of the ship.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/cooldown'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def dock_ship(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Attempt to dock your ship at its current location. Docking will only succeed if your ship is capable of docking at the time of the request.
        
        Docked ships can access elements in their current location, such as the market or a shipyard, but cannot do actions that require the ship to be above surface such as navigating or extracting.
        
        The endpoint is idempotent - successive calls will succeed even if the ship is already docked.

        Args:
            shipSymbol (str): The symbol of the ship.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/dock'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def extract_resources(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Extract resources from a waypoint that can be extracted, such as asteroid fields, into your ship. Send an optional survey as the payload to target specific yields.
        
        The ship must be in orbit to be able to extract and must have mining equipments installed that can extract goods, such as the `Gas Siphon` mount for gas-based goods or `Mining Laser` mount for ore-based goods.
        
        The survey property is now deprecated. See the `extract/survey` endpoint for more details.

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/extract'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def extract_resources_with_survey(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Use a survey when extracting resources from a waypoint. This endpoint requires a survey as the payload, which allows your ship to extract specific yields.
        
        Send the full survey object as the payload which will be validated according to the signature. If the signature is invalid, or any properties of the survey are changed, the request will fail.

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/extract/survey'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def jettison(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Jettison cargo from your ship's cargo hold.

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/jettison'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def jump_ship(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Jump your ship instantly to a target connected waypoint. The ship must be in orbit to execute a jump.
        
        A unit of antimatter is purchased and consumed from the market when jumping. The price of antimatter is determined by the market and is subject to change. A ship can only jump to connected waypoints

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/jump'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_mounts(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Get the mounts installed on a ship.

        Args:
            shipSymbol (str): The ship's symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/mounts'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def install_mount(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Install a mount on a ship.
        
        In order to install a mount, the ship must be docked and located in a waypoint that has a `Shipyard` trait. The ship also must have the mount to install in its cargo hold.
        
        An installation fee will be deduced by the Shipyard for installing the mount on the ship. 

        Args:
            shipSymbol (str): The ship's symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/mounts/install'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def remove_mount(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Remove a mount from a ship.
        
        The ship must be docked in a waypoint that has the `Shipyard` trait, and must have the desired mount that it wish to remove installed.
        
        A removal fee will be deduced from the agent by the Shipyard.

        Args:
            shipSymbol (str): The ship's symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/mounts/remove'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_ship_nav(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Get the current nav status of a ship.

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/nav'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def patch_ship_nav(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Update the nav configuration of a ship.
        
        Currently only supports configuring the Flight Mode of the ship, which affects its speed and fuel consumption.

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/nav'

        # Make the request
        response = self._patch(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def navigate_ship(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Navigate to a target destination. The ship must be in orbit to use this function. The destination waypoint must be within the same system as the ship's current location. Navigating will consume the necessary fuel from the ship's manifest based on the distance to the target waypoint.
        
        The returned response will detail the route information including the expected time of arrival. Most ship actions are unavailable until the ship has arrived at it's destination.
        
        To travel between systems, see the ship's Warp or Jump actions.

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/navigate'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def negotiateContract(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Negotiate a new contract with the HQ.
        
        In order to negotiate a new contract, an agent must not have ongoing or offered contracts over the allowed maximum amount. Currently the maximum contracts an agent can have at a time is 1.
        
        Once a contract is negotiated, it is added to the list of contracts offered to the agent, which the agent can then accept. 
        
        The ship must be present at any waypoint with a faction present to negotiate a contract with that faction.

        Args:
            shipSymbol (str): The ship's symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/negotiate/contract'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def orbit_ship(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Attempt to move your ship into orbit at its current location. The request will only succeed if your ship is capable of moving into orbit at the time of the request.
        
        Orbiting ships are able to do actions that require the ship to be above surface such as navigating or extracting, but cannot access elements in their current waypoint, such as the market or a shipyard.
        
        The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.

        Args:
            shipSymbol (str): The symbol of the ship.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/orbit'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def purchase_cargo(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Purchase cargo from a market.
        
        The ship must be docked in a waypoint that has `Marketplace` trait, and the market must be selling a good to be able to purchase it.
        
        The maximum amount of units of a good that can be purchased in each transaction are denoted by the `tradeVolume` value of the good, which can be viewed by using the Get Market action.
        
        Purchased goods are added to the ship's cargo hold.

        Args:
            shipSymbol (str): The ship's symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/purchase'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def ship_refine(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Attempt to refine the raw materials on your ship. The request will only succeed if your ship is capable of refining at the time of the request. In order to be able to refine, a ship must have goods that can be refined and have installed a `Refinery` module that can refine it.
        
        When refining, 30 basic goods will be converted into 10 processed goods.

        Args:
            shipSymbol (str): The symbol of the ship.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/refine'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def refuel_ship(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Refuel your ship by buying fuel from the local market.
        
        Requires the ship to be docked in a waypoint that has the `Marketplace` trait, and the market must be selling fuel in order to refuel.
        
        Each fuel bought from the market replenishes 100 units in your ship's fuel.
        
        Ships will always be refuel to their frame's maximum fuel capacity when using this action.

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/refuel'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def create_ship_ship_scan(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Scan for nearby ships, retrieving information for all ships in range.
        
        Requires a ship to have the `Sensor Array` mount installed to use.
        
        The ship will enter a cooldown after using this function, during which it cannot execute certain actions.

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/scan/ships'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def create_ship_system_scan(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Scan for nearby systems, retrieving information on the systems' distance from the ship and their waypoints. Requires a ship to have the `Sensor Array` mount installed to use.
        
        The ship will enter a cooldown after using this function, during which it cannot execute certain actions.

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/scan/systems'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def create_ship_waypoint_scan(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Scan for nearby waypoints, retrieving detailed information on each waypoint in range. Scanning uncharted waypoints will allow you to ignore their uncharted state and will list the waypoints' traits.
        
        Requires a ship to have the `Sensor Array` mount installed to use.
        
        The ship will enter a cooldown after using this function, during which it cannot execute certain actions.

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/scan/waypoints'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def sell_cargo(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Sell cargo in your ship to a market that trades this cargo. The ship must be docked in a waypoint that has the `Marketplace` trait in order to use this function.

        Args:
            shipSymbol (str): Symbol of a ship.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/sell'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def siphon_resources(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Siphon gases, such as hydrocarbon, from gas giants.
        
        The ship must be in orbit to be able to siphon and must have siphon mounts and a gas processor installed.

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/siphon'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def create_survey(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Create surveys on a waypoint that can be extracted such as asteroid fields. A survey focuses on specific types of deposits from the extracted location. When ships extract using this survey, they are guaranteed to procure a high amount of one of the goods in the survey.
        
        In order to use a survey, send the entire survey details in the body of the extract request.
        
        Each survey may have multiple deposits, and if a symbol shows up more than once, that indicates a higher chance of extracting that resource.
        
        Your ship will enter a cooldown after surveying in which it is unable to perform certain actions. Surveys will eventually expire after a period of time or will be exhausted after being extracted several times based on the survey's size. Multiple ships can use the same survey for extraction.
        
        A ship must have the `Surveyor` mount installed in order to use this function.

        Args:
            shipSymbol (str): The symbol of the ship.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/survey'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def transfer_cargo(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Transfer cargo between ships.
        
        The receiving ship must be in the same waypoint as the transferring ship, and it must able to hold the additional cargo after the transfer is complete. Both ships also must be in the same state, either both are docked or both are orbiting.
        
        The response body's cargo shows the cargo of the transferring ship after the transfer is complete.

        Args:
            shipSymbol (str): The transferring ship's symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/transfer'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def warp_ship(
        self,
        shipSymbol: str
    ) -> dict:
        '''
        Warp your ship to a target destination in another system. The ship must be in orbit to use this function and must have the `Warp Drive` module installed. Warping will consume the necessary fuel from the ship's manifest.
        
        The returned response will detail the route information including the expected time of arrival. Most ship actions are unavailable until the ship has arrived at its destination.

        Args:
            shipSymbol (str): The ship symbol.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/my/ships/{shipSymbol}/warp'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def register(
        self
    ) -> dict:
        '''
        Creates a new agent and ties it to an account. 
        The agent symbol must consist of a 3-14 character string, and will be used to represent your agent. This symbol will prefix the symbol of every ship you own. Agent symbols will be cast to all uppercase characters.
        
        This new agent will be tied to a starting faction of your choice, which determines your starting location, and will be granted an authorization token, a contract with their starting faction, a command ship that can fly across space with advanced capabilities, a small probe ship that can be used for reconnaissance, and 150,000 credits.
        
        > #### Keep your token safe and secure
        >
        > Save your token during the alpha phase. There is no way to regenerate this token without starting a new agent. In the future you will be able to generate and manage your tokens from the SpaceTraders website.
        
        If you are new to SpaceTraders, It is recommended to register with the COSMIC faction, a faction that is well connected to the rest of the universe. After registering, you should try our interactive [quickstart guide](https://docs.spacetraders.io/quickstart/new-game) which will walk you through basic API requests in just a few minutes.

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/register'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_systems(
        self,
        page: int = 1,
        limit: int = 10
    ) -> dict:
        '''
        Return a paginated list of all systems.

        Args:
            page (int): What entry offset to request. Default: 1
            limit (int): How many entries to return per page. Default: 10

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/systems'

        # Prepare the parameters
        params = dict()

        # Add the parameters to the parameters dict
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit

        # Make the request
        response = self._get(url=url, params=params)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_system(
        self,
        systemSymbol: str = 'X1-OE'
    ) -> dict:
        '''
        Get the details of a system.

        Args:
            systemSymbol (str): The system symbol. Default: 'X1-OE'

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/systems/{systemSymbol}'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_system_waypoints(
        self,
        systemSymbol: str,
        type: str,
        traits: str,
        page: int = 1,
        limit: int = 10
    ) -> dict:
        '''
        Return a paginated list of all of the waypoints for a given system.
        
        If a waypoint is uncharted, it will return the `Uncharted` trait instead of its actual traits.

        Args:
            systemSymbol (str): The system symbol
            type (str): Filter waypoints by type.
            traits (str): Filter waypoints by one or more traits.
            page (int): What entry offset to request. Default: 1
            limit (int): How many entries to return per page. Default: 10

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/systems/{systemSymbol}/waypoints'

        # Prepare the parameters
        params = dict()

        # Add the parameters to the parameters dict
        if type is not None:
            params['type'] = type
        if traits is not None:
            params['traits'] = traits
        if page is not None:
            params['page'] = page
        if limit is not None:
            params['limit'] = limit

        # Make the request
        response = self._get(url=url, params=params)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_waypoint(
        self,
        systemSymbol: str,
        waypointSymbol: str
    ) -> dict:
        '''
        View the details of a waypoint.
        
        If the waypoint is uncharted, it will return the 'Uncharted' trait instead of its actual traits.

        Args:
            systemSymbol (str): The system symbol
            waypointSymbol (str): The waypoint symbol

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/systems/{systemSymbol}/waypoints/{waypointSymbol}'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_construction(
        self,
        systemSymbol: str,
        waypointSymbol: str
    ) -> dict:
        '''
        Get construction details for a waypoint. Requires a waypoint with a property of `isUnderConstruction` to be true.

        Args:
            systemSymbol (str): The system symbol
            waypointSymbol (str): The waypoint symbol

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/systems/{systemSymbol}/waypoints/{waypointSymbol}/construction'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def supply_construction(
        self,
        systemSymbol: str,
        waypointSymbol: str
    ) -> dict:
        '''
        Supply a construction site with the specified good. Requires a waypoint with a property of `isUnderConstruction` to be true.
        
        The good must be in your ship's cargo. The good will be removed from your ship's cargo and added to the construction site's materials.

        Args:
            systemSymbol (str): The system symbol
            waypointSymbol (str): The waypoint symbol

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/systems/{systemSymbol}/waypoints/{waypointSymbol}/construction/supply'

        # Make the request
        response = self._post(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_jump_gate(
        self,
        systemSymbol: str,
        waypointSymbol: str
    ) -> dict:
        '''
        Get jump gate details for a waypoint. Requires a waypoint of type `JUMP_GATE` to use.
        
        Waypoints connected to this jump gate can be 

        Args:
            systemSymbol (str): The system symbol
            waypointSymbol (str): The waypoint symbol

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/systems/{systemSymbol}/waypoints/{waypointSymbol}/jump-gate'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_market(
        self,
        systemSymbol: str,
        waypointSymbol: str
    ) -> dict:
        '''
        Retrieve imports, exports and exchange data from a marketplace. Requires a waypoint that has the `Marketplace` trait to use.
        
        Send a ship to the waypoint to access trade good prices and recent transactions. Refer to the [Market Overview page](https://docs.spacetraders.io/game-concepts/markets) to gain better a understanding of the market in the game.

        Args:
            systemSymbol (str): The system symbol
            waypointSymbol (str): The waypoint symbol

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/systems/{systemSymbol}/waypoints/{waypointSymbol}/market'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


    def get_shipyard(
        self,
        systemSymbol: str,
        waypointSymbol: str
    ) -> dict:
        '''
        Get the shipyard for a waypoint. Requires a waypoint that has the `Shipyard` trait to use. Send a ship to the waypoint to access data on ships that are currently available for purchase and recent transactions.

        Args:
            systemSymbol (str): The system symbol
            waypointSymbol (str): The waypoint symbol

        Returns:
            dict: The response from the server
        '''

        # Prepare the url
        url = self.url + f'/systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard'

        # Make the request
        response = self._get(url=url)

        # Check if the request was successful
        response.raise_for_status()

        # Return the response
        return response.json()


