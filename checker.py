#!/usr/bin/env python3

# Warning, this script is a PoC and should not substitute a fully featured password checker

def checkPassword(password):
    points = 0
    
    special_characters = "!@#$%^&*()-_+=<>?,./;:[]{}|`~"

    if len(password) >= 8:
        points += 1
    elif len(password) >= 16:
        points += 2

    if (any(char.isupper() for char in password) and any(char.islower() for char in password)):
        points += 1
    elif (any(char.isupper() for char in password) or any(char.islower() for char in password)):
        points += 0.5

    if any(char.isdigit() for char in password):
        points += 0.5

    if any(char in special_characters for char in password):
        points += 1

    return points

def main():
    print("WARNING: This script is a proof of concept (POC) and should not be used as a substitute for a fully featured password checker that checks entropy.\n")
    password = input("Enter password to check: ")

    if password:
        points = checkPassword(password)
    
        if points == 6:
            print("Very Strong")
        elif points >= 4:
            print("Strong")
        elif points >= 2:
            print("Moderate")
        elif points >= 1:
            print("Weak")
        else:
            print("Very Weak")
    else:
        print("No password provided.")

if __name__ == "__main__":
    main()