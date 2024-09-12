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

dict_weathers = pipe(
    list_targets,
    lambda li: reduce(
        lambda acc, target: {
            **acc, target.target_city: get_weather(target.target_city)
        }, li, {}
    ),
    dict
)
for target in list_targets:
    target.distans = haversine_distance(lat, lon, float(get_in([[target.target_city],[0],["lat"]], dict_weathers)), float(get_in([[target.target_city],[0],["lon"]], dict_weathers)))

print(list_targets)
print(list_pilots)
print(list_aircrafts)
print(dict_weathers)

all_miss = top_missions_with_model(list_targets, list_pilots, list_aircrafts)
print(all_miss)
