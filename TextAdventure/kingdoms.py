class Kingdoms:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Drone(Kingdoms):
    def __init__(self):
        super().__init__(name="Drone Army", hp=1000, damage=600)
 
class Targaryen(Kingdoms):
    def __init__(self):
        super().__init__(name="Targaryen Dragons", hp=10000, damage=8000)

class Baretheon(Kingdoms):
    def __init__(self):
        super().__init__(name="Baretheon", hp=4000, damage=2500)

class Stark(Kingdoms):
    def __init__(self):
        super().__init__(name="Stark", hp=6000, damage=5000)