from repository.json_repository import (read_json,
                                        convert_from_json_to_aircraft,
                                        convert_from_json_to_pilot,
                                        convert_from_json_to_target)
from toolz import pipe, partial, reduce, get_in
from api.weather_api import get_weather
from service.home_controller import top_missions_with_model, haversine_distance

if __name__ == '__main__':
    pass

lat = 32.6307267
lon = 35.3488686

pilots = read_json("./data_bace/pilots.json")
aircrafts = read_json("./data_bace/aircrafts.json")
targets = read_json("./data_bace/targets.json")
list_pilots = list(map(convert_from_json_to_pilot, pilots))
list_aircrafts = list(map(convert_from_json_to_aircraft, aircrafts))
list_targets = list(map(convert_from_json_to_target, targets))

dict_weathers = {target.target_city: get_weather(target.target_city) for target in list_targets}

def get_weather_with_distana():
    for target in list_targets:
        lat_value = dict_weathers[target.target_city][0]["lat"]
        lon_value = dict_weathers[target.target_city][0]["lon"]
        target.distans = haversine_distance(lat, lon, float(lat_value), float(lon_value))
    return
print(list_targets)
print(list_pilots)
print(list_aircrafts)
print(dict_weathers)

all_miss = top_missions_with_model(list_targets, list_pilots, list_aircrafts)
print(all_miss)
