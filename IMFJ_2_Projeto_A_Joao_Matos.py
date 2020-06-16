import math

print("What problem do you want to solve?")
print("1. Floatation")
print("2. Springs")

def main():
    while(True):
        userIn = input().replace(" ", "")

        if (userIn == "1"):
            program = 1
            break
        
        elif (userIn == "2"):
            program = 2
            break

        else:
            print("Please choose 1 or 2")

