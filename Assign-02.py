#!/usr/bin/env python3
# Created by: Paterry Baptichon
# Created on: 2022-03-31
# This program calculates area of a pentagon

def main():
    # This function calculates the area of a pentagon
    print("Finding the Surface area of a Pentagon.")
    base = int(input("Enter the base of the pentagon (cm): "))
    height = int(input("Enter the height of the pentagon (cm): "))
    side_lenght = int(input("Enter the side lenghts of pentagon (cm): "))
    # process
    area = (1/2)*base*height
    perimeter = 5 * (side_lenght)
    # Output
    print("")
    print("Area is {}cm^2 ".format(area)  +
      " and the perimeter is {}(cm)".format(perimeter))

    #Ask user if they want to calculate again
    print("Would you like to try with a again")
    user_answer = str(input("Y or N:"))

    if(user_answer == ("Y") or (user_answer ==  "y")):
        main()
        
if __name__=="__main__":
    main()
    
