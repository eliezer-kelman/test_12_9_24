import json
from models.pilots import Pilot
from models.aircrafts import Aircraft
from models.targets import Target

def read_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error {e}")
        return []

def convert_from_json_to_pilot(json):
    return Pilot(
        json["name"],
        json["skill"]
    )

def convert_from_json_to_aircraft(json):
    return Aircraft(
        json["type"],
        json["speed"],
        json["puel_capacity"]
    )

def convert_from_json_to_target(json):
    return Target(
        json["Target City"],
        json["Priority"]
    )
