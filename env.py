"""
Load environment variables from the .env file or process environment.

Dependencies used: dotenv

How to install dependencies: run 'pip3 install python-dotenv'

"""

import os
import dotenv

__authors__ = ["Mustafa Aljumayli"]

# Load environment variables from .env file upon module start
dotenv.load_dotenv(f"{os.path.dirname(__file__)}/.env", verbose=True)

def getenv(variable: any) -> any:
    """Get value of environment variable or raise an error if undefined.

    Unlike `os.getenv`, our application expects all environment variables it needs to be defined
    and we intentionally fast error out with a diagnostic message to avoid scenarios of running
    the application when expected environment variables are not set.
    """
    value = os.getenv(variable)
    if value is not None:
        return value
    else:
        raise NameError(f"Error: {variable} Environment Variable not Defined")