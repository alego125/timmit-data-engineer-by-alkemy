"""Module that create models of object that will be use in structure of
requests body in the endpoints
"""

from pydantic import BaseModel


class Customers(BaseModel):
    name: str
    age: int
    email: str
    adress: str
    zip_code: str
