import math

def Main():
    print("What problem do you want to solve?")
    print("1. Floatation.")
    print("2. Springs.")

    while(True):
        program = int(input())

        if (program in [1, 2]):
            break

        else:
            print("Insert a valid option [1] or [2].")

    
    if (program == 1):
        ProgramOne()
    elif (program == 2):
        ProgramTwo()       


def ProgramOne():
    gravity = float(input("Insert the desired gravity (negative): "))
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
        print("The object would float at {:.2f} meters with these conditions.\n".format(objectHeightImmersed))
        print("You can change the initial values with 'set [property] [value]' or 'exit' the program.")
        print("[property] can be 'gravity', 'fluid density', 'density', 'volume' or 'mass'.")

        userIn = input().lower().split()

        if (userIn[0] == "exit"):
            break

        elif (userIn[0] == "set"):
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

            elif (userIn[1] == "fluiddensity" or userIn[1] == "fluidensity"):
                fluidDensity = float(userIn[2])

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
    gravity = float(input("Insert the desired gravity (negative): "))
    objectMass = float(input("Insert the desired object mass: "))
    baseLength = float(input("Insert the desired base spring length: "))
    springConst = float(input("Insert the desired spring constant: "))

    while(True):
        objectGravity = objectMass * gravity
        stretchedLength = (objectGravity / (-springConst)) + baseLength

        print("\nThe object has {:.2f} mass and the gravity is {:.2f}.".format(objectMass, gravity))
        print("The base spring length is {:.2f} and it's constant is {:.2f}.".format(baseLength, springConst))
        print("The spring would stretch to {:.2f} meters.\n".format(stretchedLength))
        print("You can change the initial values with 'set [property] [value]' or 'exit' the program.")
        print("[property] can be 'gravity', 'mass', 'length' or 'constant'.")

        userIn = input().lower().split()

        if (userIn[0] == "exit"):
            break

        elif (userIn[0] == "set"):
            if (userIn[1] == "gravity"):
                gravity = float(userIn[2])
            
            elif (userIn[1] == "mass"):
                objectMass = float(userIn[2])
            
            elif (userIn[1] == "length"):
                baseLength = float(userIn[2])
            
            elif (userIn[1] == "constant"):
                springConst = float(userIn[2])


Main()
