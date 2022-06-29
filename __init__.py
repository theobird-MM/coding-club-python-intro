import sys
import random

def proceed():
    a = input("Proceed? ").lower()
    
    if a in ["yes","y"]:
        print("Then let's go.")
    if len(a) > 8:
        print("There's no need to be rude.")
        exit() 
    else:
        print("Very well.")
        exit()

## ---- Python Boolean Tests
testString = "sarah's chronicles commencing"
print(testString.title())

testPass = False
a = 0
b = 75
c = random.randrange(50,100)
testIn = "Input's"

print("We need a value, Sarah")

while testPass is False:
    a = int(input())

    if a < b and a != c:
        print(testIn, "too smol.")
    elif a == c:
        print(testIn, "the same as Hoggle's.")
    else:
        testPass = True
        print(f"{a} is good, Hoggle's was {c}.\nYou may continue...")
        break

# proceed() ## Manual check for continuing

## ---- Going to planets
print("Where do you want to go?")
    
planets = ["mercury", "venus", "mars","jupiter", "saturn", "uranus","neptune"]
planetoids = ["pluto", "eris", "ceres", "ganymede"]
planetGravity = [0.378,0.907,0.377,2.36,0.916,0.889,1.12,0.071]

destination = ""
destinationConfirmed = False

while destinationConfirmed is False:
    destination = input().lower()
    
    if destination in planets:
        print("Excellent. We are going to ", destination)
        destinationConfirmed = True
    elif destination in planetoids:
        print("That is not a planet, but if you insist...")
        destinationConfirmed = True
    elif destination == "earth":
        print("We are already there. Choose somewhere else.")
    elif destination == "moon":
        print("Come on, Sarah, something more exciting than that.")
    else:
        print("A planet, Sarah.")
    if destinationConfirmed:
        break

proceed() ## Manual check for continuing









