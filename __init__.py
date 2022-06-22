import sys
import random

def proceed():
    print("Proceed?")
    a = input()
    if a == "No":
        exit()

## Python Boolean Tests
testString = "boolean testing commencing"
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

proceed()

## Going to planets
planets = ["Mercury", "Venus", "Mars","Jupiter", "Saturn", "Uranus","Neptune"]
planetoids = ["Pluto", "Eris", "Ceres", "Ganymede"]
planetGravity = [0.378,0.907,0.377,2.36,0.916,0.889,1.12,0.071]

if testPass:
    print("Where do you want to go?")

destination = 0
destinationConfirmed = False

while destinationConfirmed is False:
    destination = input()
    
    if destination in planets:
        print("Excellent. We are going to ", destination)
        destinationConfirmed = True
    elif destination in planetoids:
        print("That is not a planet, but if you insist...")
        destinationConfirmed = True
    else:
        print("A planet, Sarah.")
    if destinationConfirmed:
        break

proceed()




