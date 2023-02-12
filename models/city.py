#!/usr/bin/python3
"""
creating class city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city
    """

    state_id = ""
    name = ""
#!/usr/bin/python3
"""
City class, a subclass of BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A subclass of BaseModel class
    Public class attributes:
        state_id: (str) will be State.id
        name:     (str)
    """
    state_id = ""
    name = ""
