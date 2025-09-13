import random

class notTamagotchi:
    
    def __init__(self, name):
        self.name = name    
        self.happiness = 50
        self.hunger = 50
        self.alive = True
        
    def clock_tick(self):
        """Simulates the passage of time."""
        self.hunger += 5
        self.happiness -= 5
        
        # Check if the pet has died from neglect
        if self.hunger > 100 or self.happiness < 0:
            self.alive = False
        
    
    def feed(self):
        self.hunger = max(0, self.hunger - 20)
            
    def  play(self):
        self.happiness = min(100, self.happiness + 20)
            
    def sleep(self):
        self.energy = min(100, self.energy + 30)
            
    def get_status(self):
        """Returns a string describing the pet's current state."""
        if not self.alive:
            return f"{self.name} is no longer with us. R.I.P."
        
        if self.hunger > 70:
            mood = "hungry"
        elif self.happiness < 30:
            mood = "bored"
        else:
            mood = "happy"
        
        return f"{self.name} is feeling {mood}."
        