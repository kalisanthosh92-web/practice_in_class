class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Bark!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Meow!"        

class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Chirp!"

class Fish:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says ...!"    

D1 = Dog("Buddy")
C1 = Cat("Whiskers")
B1 = Bird("Tweety")
F1 = Fish("Nemo")

def animal_sound(animal):
    print(animal.name, ":" , animal.speak())
   
#animal_sound(D1)
#animal_sound(C1)
#animal_sound(B1)
#animal_sound(F1)

animals = [D1, C1, B1, F1]
for animal in animals: 
    print(animal.name, ":", animal.speak())
