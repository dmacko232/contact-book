from typing import Tuple
from dataclasses import dataclass


@dataclass
class Contact:
    """Class used to represent a contact book stored in database."""

    id: int
    name: str
    address: str
    phone_number: str
    email: str


@dataclass
class CreateContact:
    """Class used to represent data needed to create a contact book."""

    name: str
    address: str
    phone_number: str
    email: str
