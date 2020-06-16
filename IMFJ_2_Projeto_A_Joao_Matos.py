import math

def main():
    print("What problem do you want to solve?")
    print("1. Floatation")
    print("2. Springs")

    while(True):
        program = int(input())

        if (program in [1, 2]):
            break

        else:
            print("Insert a valid option [1] or [2]")

    Program(program)

    
def Program(i):
    if (i == 1):
        ProgramOne()
    elif (i == 2):
        ProgramTwo()
        


def ProgramOne():
    gravity = float(input("Insert the desired gravity: "))

    fluidDensity = float(input("Insert the desired fluid density: "))

    objectDensity = float(input("Insert the desired object density: "))

    objectVolume = float(input("Insert the desired object volume: "))

    objectMass = objectDensity * objectVolume

    objectEdge = objectVolume**(1/3)

    objectGravity = objectMass * gravity

    objectVolumeImmersed = objectGravity / (fluidDensity * gravity)

    objectHeightImmersed = objectVolumeImmersed / (objectEdge**2)

    while(True):
        print("\nThe object has {:.2f} mass, {:.2f} density and {:.2f} volume.".format(objectMass, objectDensity, objectVolume))
        print("The fluid has a density of {:.2f} and the gravity force is {:.2f}.".format(fluidDensity, gravity))
        print("The object would float at {:.2f} with these conditions.\n".format(objectHeightImmersed))

        print("You can change the initial values with 'set [property] [value]'.")

        userIn = input().split()

        if (userIn[0] == "set"):
            if (userIn[1] == "gravity"):
                gravity = float(userIn[2])

                objectGravity = objectMass * gravity
                objectVolumeImmersed = objectGravity / (fluidDensity * gravity)
                objectHeightImmersed = objectVolumeImmersed / (objectEdge**2)

            
            elif (userIn[1] == "fluid"):
                if (userIn[2] == "density"):
                    fluidDensity = float(userIn[3])

                    objectVolumeImmersed = objectGravity / (fluidDensity * gravity)
                    objectHeightImmersed = objectVolumeImmersed / (objectEdge**2)
            
            elif (userIn[1] == "density"):
                objectDensity = float(userIn[2])

                objectMass = objectDensity * objectVolume
                objectGravity = objectMass * gravity
                objectVolumeImmersed = objectGravity / (fluidDensity * gravity)
                objectHeightImmersed = objectVolumeImmersed / (objectEdge**2)
            
            elif (userIn[1] == "volume"):
                objectVolume = float(userIn[2])

                objectEdge = objectVolume**(1/3)
                objectMass = objectDensity * objectVolume
                objectGravity = objectMass * gravity
                objectVolumeImmersed = objectGravity / (fluidDensity * gravity)
                objectHeightImmersed = objectVolumeImmersed / (objectEdge**2)
            
            elif (userIn[1] == "mass"):
                objectMass = float(userIn[2])

                objectVolume = objectMass / objectDensity
                objectEdge = objectVolume ** (1/3)
                objectGravity = objectMass * gravity
                objectVolumeImmersed = objectGravity / (fluidDensity * gravity)
                objectHeightImmersed = objectVolumeImmersed / (objectEdge**2)


def ProgramTwo():
    ...


main()
