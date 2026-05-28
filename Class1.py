class Car:
    def __init__(self,make,model,colour):
        self.make = make
        self.model = model
        self.colour = colour
        self.speed = 0
    
    def drive(self): 
        print(f'The {self.colour} {self.make} {self.model} is driving!') 

    def accelerate(self, amount):  # Method 
        self.speed += amount 
        print(f"The car's new speed is {self.speed} km/h.") 

class SportsCar(Car):
    def __init__(self, make, model, colour, turbo):
        super().__init__(make, model, colour)
        self.turbo = turbo

sports = SportsCar("BMW","M3","Red","Yes")
sports.accelerate(100)