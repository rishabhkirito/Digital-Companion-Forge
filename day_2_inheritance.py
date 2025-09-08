class DigitalCompanion:
    def __init__(self, name ,personality,creator):
        self.name = name
        self.energy_level = 100 
        self.personality = personality
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
        #print(f"Mood: {self.mood}")
        print(f"Trait: {self.personality}")
        print(f"Creator: {self.creator}")

    def set_mood(self, new_mood):
        self.mood = new_mood
        print(f"{self.name}:Mood is {self.mood}")

    def get_mood(self):
        return self.mood
    
class codingComapanion(DigitalCompanion):
    def __init__(self,name,creator,known_languages):
        super().__init__(name=name,creator=creator,personality = "Coder")

        self.known_languages = known_languages

    def write_code(self,language):
        if language in self.known_languages:
            print(f"{language} is the coding language used by{self.name}")
        else:
            print(f"{self.name} hasn't learnt to code in this language yet")
        
class GamingCompanion(DigitalCompanion):
    def __init__(self,name,creator,favourite_game):
        super().__init__(name = name,personality = "competitive",creator = creator)

        self.favourite_game = favourite_game

    def game_mode(self,game):
        if game == self.favourite_game:
            print(f"{self.name} is playing his favourite game{game}")
        else:
            print(f"{self.name} has skill issues in this game")

blaze = codingComapanion(name = "blaze",creator = "Kirito",known_languages = ["Python","TypeScript"])
blaze.write_code("Python")
blaze.write_code("TypeScript")
blaze.write_code("Java")
blaze.status_report()

powder = GamingCompanion(name="powder",creator="kirito",favourite_game="Insomaniac Spider-Man")
powder.game_mode("Insomaniac Spider-Man")
powder.game_mode("Metro Exodus")

