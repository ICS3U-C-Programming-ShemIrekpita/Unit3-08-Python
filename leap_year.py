#!/usr/bin/env python3
# Created by: Shem
# Created on: 11/1/2025
# This program checks if a year is a leap year

def main():
# Ask the user to enter a year
    user_input = input("Enter a year: ")
    try:
# Try to convert input to integer!
        year = int(user_input)
# Leap year logic
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(year, "is a leap year!")
                else:
                    print(year, "is not a leap year.")
            else:
                print(year, "is a leap year!")
        else:
            print(year, "is not a leap year.")
    except ValueError:
# For when user enters something that is not a number
        print(user_input, "is not a valid number.")
# This ensures the program starts
if __name__ == "__main__":
    main()