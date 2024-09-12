class Target:
    def __init__(self, target_city, priority, distans=None, weather=None):
        self.target_city = target_city
        self.priority = priority
        self.distans = distans
        self.weather = weather

    def __repr__(self):
        return f"Target: ({self.target_city}, {self.priority}, {self.distans}, {self.weather}) "
