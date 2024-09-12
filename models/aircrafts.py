class Aircraft:
    def __init__(self, type, speed, puel_capacity):
        self.type = type
        self.speed = speed
        self.puel_capacity = puel_capacity

    def __repr__(self):
        return f"Aircraft: ({self.type}, {self.speed}, {self.puel_capacity}) "
