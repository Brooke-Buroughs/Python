class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=health
        self.energy=energy
    def sleep(self, energy):
        self.energy+=energy
        print(f"Energy:{self.energy}")
        return self
    def eat(self, energy, health):
        