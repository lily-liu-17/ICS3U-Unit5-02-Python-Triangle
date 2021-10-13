#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program will calculate area of triangle


def calcutate_area(length, height):
    # This function will calculate area of triangle
    # process & output
    area_triangle = round((length * height) / 2, 2)
    print("")
    print("The area of the triangle is {0} cm²".format(area_triangle))


def main():
    # this is he main function
    length_user = input("Enter the base length of the triangle (cm) : ")
    height_user = input("Enter the height of the triangle (cm) : ")

    try:
        length_user = float(length_user)
        height_user = float(height_user)
        # call functions
        calcutate_area(length_user, height_user)
    except (Exception):
        print("Invalid input")

    print("\nDone.")


if __name__ == "__main__":
    main()
