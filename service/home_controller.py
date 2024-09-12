from toolz import pipe, reduce, partition
from functools import partial
from api.weather_api import get_weather
from toolz import pipe, partial, map
from repository.json_repository import convert_from_json_to_pilot
from models.missions import Mission
import math

def normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)

def top_missions_with_model(targets, pilots, aicrafts):
    all_combinations = [(target, pilot, aicraft) for target in targets for pilot in pilots for aicraft in aicrafts]
    all_missions = pipe(
        all_combinations,
        partial(map, lambda x: Mission(x[0], x[1], x[2])),
        partial(filter, lambda x: x.relative_distance > 0 and x.relative_distance < 1),
        lambda li: list(calculate_score_with_model(mission) for mission in li),
        partial(sorted, key=lambda x: x.mission_fit_score, reverse=True)
    )
    return all_missions

def calculate_score_with_model(mission):
    weather_score = normalize(mission.weather, 1, 5)
    pilot_skill_score = normalize(mission.skill, 1, 10)
    priority_score = normalize(mission.priority, 1, 5)
    mission.mission_fit_score = (
            0.2 * mission.relative_distance +
            0.25 * weather_score +
            0.25 * pilot_skill_score +
            0.3 * priority_score)
    return mission

# Function to calculate the distance between two coordinates using the Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0  # Radius of the Earth in kilometers
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance
