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

# Slicing - works for both lists and tuples
piano_keys=['a','b','c','d','e','f']
print(piano_keys[1:4]) # 1 included and 4 excluded index
print(piano_keys[2:]) # all elements from 2nd index
print(piano_keys[:4]) # all elements till 4th index, 4th index excluded
print(piano_keys[1:5:2]) # third number specifies increment during slicing 
print(piano_keys[::2]) # every alt item in list
print(piano_keys[::-1]) # reverses list