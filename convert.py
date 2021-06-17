'''Written by JT Vannoy Feb 14 2018
Program converts inches/hour to miles/hour
Program asks name to personalize experience
'''

# the title is printed and program moves to newline
title = "Converter Program 1.0 \n"
print(title) 

# name is learned and welcome message is printed
name = input("Enter your first name: ")
last = input("Enter your last name: ")
print("Hello,", name, last+"!\n")

# program explains purpose and calculates the answer
print("This program converts inches per hour to miles per hour.")
init_value = float(input("Enter the number of inches per hour to be converted: "))
result = init_value / 63360

print(init_value, "inches/hour is equal to", result, "miles/hour\n")

print("Thank you for using this program", name+"!")
print