import sys
import random

userInput = ""

#planets = {"name":"earth","gravity":1.00,"moons":1}
    
planet = ["mercury", "venus", "mars","jupiter", "saturn", "uranus","neptune","pluto", "eris", "ceres", "ganymede"]
planetGravity = [0.378,0.907,0.377,2.36,0.916,0.889,1.12,0.071,0.84,0.028,0.146]


for i in range(len(planet)):
    # planets = {}
    print(planetGravity[i])




exit()

def proceed():
    userInput = input("Proceed? ").lower()
    
    if userInput in ["yes","y"]:
        print("Then let's go.")
    if len(userInput) > 8:
        print("There's no need to be rude.")
        exit() 
    else:
        print("Very well.")
        exit()

## ---- Python Boolean Tests
testString = "sarah's chronicles commencing"
print(testString.title())

testPass = False
testInput = 0
testLowerLimit = 75
testHoggle = random.randrange(50,100)
testIn = "Input's"
testPatience = 1

print("We need a value, Sarah")

while testPass is False:
    testInput = int(input())

    if testInput < testLowerLimit and testInput != testHoggle:
        print(testIn, "too smol.")
        if testPatience > 2:
            print("Pick something bigger, Sarah...")
    elif testInput == testHoggle:
        print(testIn, "the same as Hoggle's.")
    else:
        testPass = True
        if testPatience > 2:
            print(f"Finally! A big number. Hoggle only picked {testHoggle}.")
        else:
            print(f"{testInput} is good, Hoggle's was {testHoggle}.")
        print("You may continue...")
        break
    testPatience = testPatience + 1

## proceed() ## Manual check for continuing

## ---- Going to planet
print("Where do you want to go?")

#planets = {"name":"earth","gravity":1.00,"moons":1}
    
planet = ["mercury", "venus", "mars","jupiter", "saturn", "uranus","neptune","pluto", "eris", "ceres", "ganymede"]
planetGravity = [0.378,0.907,0.377,2.36,0.916,0.889,1.12,0.071,0.84,0.028,0.146]

for x in planet:
    planets = {}

destinationRequest = ""
destinationConfirmed = False
destinationSelection = ""
destinationsQueried = 0

while destinationConfirmed is False:
    destinationRequest = input().lower()
    
    if destinationRequest in planet[0:7]:
        print("Excellent. We are going to ", destinationRequest)
        destinationConfirmed = True
    elif destinationRequest in planet[8:10]:
        print("That is not a planet, but if you insist...")
        destinationConfirmed = True
    elif destinationRequest == "earth":
        print(f"We are already there. Choose somewhere else. ({destinationsQueried})")
    elif destinationRequest == "moon":
        print(f"Come on, Sarah, something more exciting than that. ({destinationsQueried})")
    else:
        print(f"A planet, Sarah. ({destinationsQueried})")
    if destinationConfirmed:
        destinationSelection = planet.index(destinationRequest)
        break
    destinationsQueried = destinationsQueried + 1

## proceed() ## Manual check for continuing

## ---- Preparing for the selected planet.

print(f"Are you aware of the gravity on {planet[destinationSelection].title()}?")

userInput = input().lower()





