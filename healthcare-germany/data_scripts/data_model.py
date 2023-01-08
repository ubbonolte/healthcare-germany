from dataclasses import dataclass


@dataclass()
class Hospital:
    name: str
    zip_code: str
    place: str
    street: str
