class DigitalCompanion:
    def __init__(self, name ,personality,creator):
        self.name = name
        self.energy_level = 100 
        self.personality = personality
        self.mood = "Happy"
        self.creator = creator

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
        
    def creator_name(self):
        print(f"{self.name}:My creator is {self.creator}")
    
    def status_report(self):
        print(f"Name: {self.name}")
        print(f"Mood: {self.mood}")
        print(f"Trait: {self.personality}")
        print(f"Creator: {self.creator}")

    def set_mood(self, new_mood):
        self.mood = new_mood
        print(f"{self.name}:Mood is {self.mood}")

    def get_mood(self):
        return self.mood

#creating an object(an instance) of the class
Kael = DigitalCompanion("Kael","Fuunny","Kirito")
print("\n"+ "---"*5 + "First Object" + "---"*5+ "\n")

#using one of it's capabilites
Kael.greet()
Kael.emotion()
Kael.energy()
Kael.trait()
Kael.creator_name()

print("\n"+ "---"*5 + "Second Object" + "---"*5+ "\n")

nexus = DigitalCompanion(
    name = "nexus",
    personality = "analytical",    
    creator = "Rishabh"
)
nexus.greet()
nexus.emotion()
nexus.energy()
nexus.trait()
nexus.creator_name()

print("Initaial Report Status")
Kael.status_report()
print("-" * 20)

print("Kaels updated mood")
Kael.set_mood("curious")

Kael.status_report()
print("\n"+"---"*5 +"\n")
nexus.status_report()