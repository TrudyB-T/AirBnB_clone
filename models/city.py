#!/usr/bin/python3
"""
    class City.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        Inherits from the BaseModel class

        Attributes:
                   state_id (str): string - empty string:
                                   it will be the State.id
                   name (str): string - empty string
    """
    state_id = ""
    name = ""
