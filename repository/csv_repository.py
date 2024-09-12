import csv
from typing import List
from models.missions import Mission

def write_people_to_csv(missions: List[Mission], filepath: str):
    try:
        with open(filepath, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile,
                                        fieldnames=['target_city',
                                                     'priority',
                                                     'name_pilot',
                                                     'name_warrior',
                                                     'distans',
                                                     'weather',
                                                     'skill_pilot',
                                                     'speed_warrior',
                                                     'puel_capacity',
                                                     'mission_fit_score'])
            csv_writer.writeheader()

            for mission in missions:
                csv_writer.writerow({
                    'target_city': mission.target_city,
                    'priority': mission.priority,
                    'name_pilot': mission.name_pilot,
                    'name_warrior': mission.name_warrior,
                    'distans': mission.distans,
                    'weather': mission.weather,
                    'skill_pilot': mission.skill_pilot,
                    'speed_warrior': mission.speed_warrior,
                    'puel_capacity': mission.puel_capacity,
                    'mission_fit_score': mission.mission_fit_score
                })
    except Exception as e:
        print(e)
