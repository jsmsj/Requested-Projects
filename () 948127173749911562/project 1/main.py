##### jsmsj#5252 #####
"""Imports"""

# We are offered a choice between $1,000,000 and $0.01 doubled everyday for n days.

first_option = 1000000

second_option = 0.01

days = int(input("Enter the number of days for which the money will be doubled each day : "))

second_option *= (2**days)

if first_option>second_option:
    print(f"Take $1000000 because second option will give you approximately ${round(second_option,2)}. Which is ${first_option-round(second_option,2)} less than $1000000.")
elif first_option == second_option:
    print("both options will give you same money and that is $1000000")
else:
    print(f"Choose the second option as it gives you approximately ${round(second_option,2)}. Which is ${round(second_option,2)-first_option} more than $1000000.")
