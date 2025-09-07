class DigitalCompanion:
    def __init__(self, name):
        self.name = name
        self.mood = "Happy"
        self.energy_level = 100 
        self.personality = "Funny"

    def greet(self):
        print(f"{self.name}: Hello! What can I help you with today?")

    def emotion(self):
        print(f"{self.name}:{self.mood} is my current emotion")

    def energy(self):
        if self.energy_level < 50:
            print(f"{self.name}:No energy to engage in combat")
        else:
            print(f"{self.name}:Let's keep forging")
            self.energy_level -= 20
        print(f"current energy level: {self.energy_level}")

    def trait(self):
        print(f"{self.name}:current trait{self.personality}")
        print(f"Nanooooo Banana")

#creating an object(an instance) of the class
Kael = DigitalCompanion("Kael")

#using one of it's capabilites
Kael.greet()
Kael.emotion()
Kael.energy()
Kael.trait()