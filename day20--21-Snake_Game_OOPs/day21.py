# Class inheritance
class Animal():
    def __init__(self):
        self.num_eyes=2

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Breathe through gills") # Addition to exisiting functionality inherited from super class

    def swim(self):
        print("Move in water")

nemo=Fish()
nemo.swim()
nemo.breathe() # Prints additional print statement along with print statement inherited from Animal
print(nemo.num_eyes)