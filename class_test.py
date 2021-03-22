class Mamal:
    def __init__(self, animal):
        self.animal = animal

    def attack(self):
        print(f"You attack the {self.animal}")
        self.look()

    def look(self):
        print(f"You decide to just look at the {self.animal}")


tiger = Mamal("tiger")
tiger.attack()

dolphin = Mamal("dolphin")
dolphin.attack()
dolphin.look()
