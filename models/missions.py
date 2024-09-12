class Mission:
    def __init__(self, target, pilot, aircraft, mission_fit_score=0):
        self.target_city = target.target_city
        self.priority = target.priority
        self.name_pilot = pilot.name
        self.type = aircraft.type
        self.distans = target.distans
        self.weather = 4  # target.weather
        self.skill_pilot = pilot.skill
        self.speed = aircraft.speed
        self.puel_capacity = aircraft.puel_capacity
        self.relative_distance = float(self.distans) / float(self.puel_capacity)
        self.mission_fit_score = mission_fit_score

    def __repr__(self):
        return f"Mission: ({self.target_city}, {self.priority}, {self.distans}, {self.weather}) "
