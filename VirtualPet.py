#Daniel Ogunlana
#05/06/2015
import random

class VirtualPet:
    def __init__(self,name):
        self.name = name
        self.energy = 60
        self.food = ["Tuna", "Mice", "Birds", "Wet Cat Food", "Dry Cat Food"]
        self.water = 50
        self.mood = 70
        print("I have been born my name is {0}".format(self.name))

    def eat(self,food):
        if self.energy <100:
            if food in self.food:
                if self.food == "Tuna":
                    self.energy = self.energy + 20
                elif self.food == "Mice":
                    self.energy = self.energy + 5
                elif self.food == "Birds":
                    self.energy = self.energy + 10
                elif self.food == "Wet Cat Food":
                    self.energy = self.energy + 15
                    self.water = self.water + 10
                elif self.food == "Dry Cat Food":
                    self.energy = self.energy + 25
                print("Nom Nom! I have eaten {0} and have gained".format())
                print("{0} energy".format())
                #Need an if statement for if water has been gained
                #if water has been gained the it will display how much
            else:
                self.mood = self.mood -10
                

pet_one = VirtualPet(input("Give your pet a name: "))

FeedPet = input("Do you want to feed your pet?: ")
if FeedPet.[0] == "y"
feed your pet = eat(food)
