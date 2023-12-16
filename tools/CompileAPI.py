# Lib Author: Mattia Brunelli (https://github.com/brodo97)
#
# OpenAPI Author: Joel Brubaker (joel@spacetraders.io)
# OpenAPI Source: https://raw.githubusercontent.com/SpaceTradersAPI/api-docs/main/reference/SpaceTraders.json
#
# Description: This script reads the OpenAPI json file and generates the SpaceTradersAPI.py file
#              which can be used to interact with the SpaceTraders API easily and efficiently.
#              The SpaceTradersAPI.py file is generated in the app folder.
#
# How to use: 1. Download the OpenAPI json file from https://raw.githubusercontent.com/SpaceTradersAPI/api-docs/main/reference/SpaceTraders.json
#             2. Place the OpenAPI json file in the tools folder
#             3. Run this script
#             4. Copy the SpaceTradersAPI.py file from the app folder to the app folder in your project
#             5. Import the SpaceTradersAPI.py file in your project
#             6. Use the SpaceTradersAPI.py file in your project
#
# Note: This script is not perfect and might not work for all OpenAPI json files.
#       If you find any bugs, please report them on the GitHub repository.
#       If you want to add a feature, please create a pull request on the GitHub repository.
#

import json
from icecream import ic as print

space_traders_api_file = open("app/SpaceTradersAPI.py", "w")


def read_json(file: str) -> dict:
    """ Reads a json file and returns the data as a dict

    Args:
        file (str): The path to the json file

    Returns:
        dict: The data from the json file
    """

    # Open the file and return the data
    with open(file, "r") as f:
        return json.load(f)


def write_line(line: str) -> None:
    """ Writes a line to the SpaceTradersAPI.py file

    Args:
        line (str): The line to write to the file
    """

    space_traders_api_file.write(f"{line}\n")


def write_header(data: dict) -> None:
    """ Writes the header to the SpaceTradersAPI.py file

    Args:
        data (dict): The data from the json file
    """

    write_line("#")
    write_line("# Lib Author: Mattia Brunelli (https://github.com/brodo97)")
    write_line("#")
    write_line("# API Author: Joel Brubaker (joel@spacetraders.io)")
    write_line("#\n")

    # Write the header
    libs_to_install = ["requests"]
    for lib in libs_to_install:
        write_line(f"import {lib}")

    # Get the url of the server
    url = data["servers"][0]["url"]

    write_line(f"")
    write_line(f"class SpaceTraders:")
    write_line(f"    def __init__(self, token: str) -> None:")
    write_line(f"        self.token = token  # The token used to authenticate the user")
    write_line(f"        self.url = {url!r}  # The url of the server")
    write_line(f"")
    write_line(f"        # The session used to make requests and prepare the session methods for better readability")
    write_line(f"        self.session = requests.Session()")
    write_line(f"        self._get = self.session.get")
    write_line(f"        self._post = self.session.post")
    write_line(f"        self._patch = self.session.patch")
    write_line(f"        self.session.headers.update({{")
    write_line(f"            'Content-Type': 'application/json',")
    write_line(f"            'Accept': 'application/json',")
    write_line(f"            'Authorization': f'Bearer {{self.token}}',")
    write_line(f"        }})")
    write_line(f"")


def write_function_header(name: str, params: dict) -> None:
    """ Writes the header of a function to the SpaceTradersAPI.py file

    Args:
        name (str): The name of the function
        params (dict): The parameters of the function
    """

    # Add the parameters to the function header
    function_arguments = ["self"]
    for param in sorted(params, key=lambda x: x["has_default"]):
        # Add the parameter to the function header
        text = f"{param['name']}: {param['parameter_fmt']}"

        # Add the default value to the function header
        if param["has_default"]:
            text += f" = {param['default']!r}"

        function_arguments.append(
            text
        )

    write_line(f"    def {name}(")

    # Loop over the function arguments
    for x, argument in enumerate(function_arguments):
        if x != len(function_arguments) - 1:
            write_line(f"        {argument},")
            continue
        write_line(f"        {argument}")
    
    write_line(f"    ) -> dict:")

def write_function_docstring(description: str, params: dict) -> None:
    """ Writes the docstring of a function to the SpaceTradersAPI.py file

    Args:
        description (str): The description of the function
        params (dict): The parameters of the function
    """

    write_line(f"        '''")

    # Add the description to the docstring
    description = description.replace("\n", "\n        ")
    write_line(f"        {description}")

    # Add the parameters to the docstring
    if len(params) > 0:
        write_line(f"")
        write_line(f"        Args:")
        # Add the parameters to the function docstring
        for param in sorted(params, key=lambda x: x["has_default"]):
            # Add the parameter to the function docstring
            text = f"{param['name']} ({param['parameter_fmt']}): {param['description']}"

            # Add the default value to the function docstring
            if param["has_default"]:
                text += f". Default: {param['default']!r}"

            write_line(f"            {text}")

    write_line(f"")
    write_line(f"        Returns:")
    write_line(f"            dict: The response from the server")

    write_line(f"        '''")


def write_function_body(name: str, url: str, action: str, params: dict) -> None:
    # Add the parameters to the function body
    function_arguments = ["self"]
    for param in sorted(params, key=lambda x: x["has_default"]):
        # Add the parameter to the function body
        text = f"{param['name']}={param['name']}"

        # Add the default value to the function body
        if param["has_default"]:
            text += f" if {param['name']} is not None else {param['default']!r}"

        function_arguments.append(
            text
        )

    write_line(f"        # Prepare the url")
    write_line(f"        url = self.url + f{url!r}")

    add_parameters = False

    # Add the parameters to the function body
    if any(param["in"] == "query" for param in params):
        write_line(f"")
        write_line(f"        # Prepare the parameters")
        write_line(f"        params = dict()")
        write_line(f"")
        write_line(f"        # Add the parameters to the parameters dict")
        for param in sorted(params, key=lambda x: x["has_default"]):
            if param["in"] == "query":
                write_line(f"        if {param['name']} is not None:")
                write_line(f"            params['{param['name']}'] = {param['name']}")
                add_parameters = True

    # Add the parameters to the function body
    write_line(f"")
    write_line(f"        # Make the request")

    # Add the parameters to the function request if there are any
    text = f"        response = self._{action}(url=url"
    if add_parameters:
        text += ", params=params)"
    else:
        text += ")"

    write_line(text)
    write_line(f"")
    write_line(f"        # Check if the request was successful")
    write_line(f"        response.raise_for_status()")

    # Add the parameters to the function body
    write_line(f"")
    write_line(f"        # Return the response")
    write_line(f"        return response.json()")

def parse_schema(schema: dict) -> str:
    if "type" in schema:
        if schema["type"] == "string":
            return "str"
        elif schema["type"] == "integer":
            return "int"
        elif schema["type"] == "boolean":
            return "bool"
        elif schema["type"] == "array":
            return "list"
        elif schema["type"] == "object":
            return "dict"
        else:
            return "str"
    else:
        return "str"

def parse_parameters(parameters: list) -> list:
    params = list()
    # Loop over the parameters
    for parameter in parameters:
        
        # Get the name of the parameter
        name = parameter["name"]
        
        # Get parameter schema and convert it to a python type
        schema = parameter["schema"]
        parameter_fmt = parse_schema(schema)

        # Get parameter description
        description = parameter["description"]

        params.append({
            "name": name,
            "parameter_fmt": parameter_fmt,
            "description": description,
            "required": parameter["required"] if "required" in parameter else False,
            "in": parameter["in"] if "in" in parameter else "query",
            "has_default": "default" in schema,
            "default": schema["default"] if "default" in schema else None
        })

    return params

def loop_over_endpoints(data: dict) -> None:
    for endpoint, endpoint_data in sorted(data["paths"].items(), key=lambda x: x[0]):
        parameters = endpoint_data.pop("parameters", [])
        for action, action_data in sorted(endpoint_data.items(), key=lambda x: x[0]):
            name = action_data["operationId"].replace("-", "_")
            url = endpoint
            params = parse_parameters(parameters)
            params.extend(parse_parameters(action_data.get("parameters", [])))

            write_function_header(
                name=name, 
                params=params
            )

            # Get the description of the action
            description = action_data["description"]

            write_function_docstring(
                description=description,
                params=params
            )
            
            write_line(f"")
            
            write_function_body(
                name=name,
                url=url,
                action=action,
                params=params
            )

            write_line(f"")
            write_line(f"")
            # print(action, action_data)

if __name__ == "__main__":
    json_data = read_json("tools/source.json")
    write_header(data=json_data)
    loop_over_endpoints(data=json_data)
    space_traders_api_file.close()