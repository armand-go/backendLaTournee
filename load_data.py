"""
Import Store data fron a json file
"""
import json


def load_data(filename: str) -> list[dict]:
    """
    Load data from a json file
    """
    with open(filename, "r") as filed:
        return json.load(filed)
