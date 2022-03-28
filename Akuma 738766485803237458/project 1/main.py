##### jsmsj#5252 #####
"""Imports"""
import sys

def get_year_level(value_list:list):
    """Function to get year level of the student"""
    i=1
    year_level = 0
    while year_level not in value_list:
        if i <=3:
            if i != 1:
                print("INVALID INPUT")
            year_level = input("Enter the year level: ")
        else:
            sys.exit()
        i+=1
    return year_level

def get_grades(subject):
    """Get grades of given subject from the user"""
    i=1
    grade = 0
    while grade < 65 or grade >100:
        if i <=3:
            if i != 1:
                print("\tINVALID INPUT")
            try:
                grade = int(input(f"\t{subject}: "))
            except:
                pass
        else:
            sys.exit()
        i+=1
    return grade

def get_remark(grade):
    """Get remark from the given grade"""
    if grade >= 65 and grade <= 74: return "Poor"
    elif grade >= 75 and grade <= 79: return "Fair"
    elif grade >= 80 and grade <= 89: return "Good"
    elif grade >= 90 and grade <= 99: return "Very Good"
    elif grade==100: return "Excellent"

last_name = input("Enter the last name: ")
first_name = input("Enter the first name: ")
year_level = get_year_level([str(i) for i in range(1,5)])
print("Input Grades:")
math_grades = get_grades("Mathematics")
science_grades = get_grades("Science")
english_grades = get_grades("English")
filipino_grades = get_grades("Filipino")
computer_grades = get_grades("Computer")
average = (math_grades + science_grades + english_grades + filipino_grades + computer_grades)/5
print()
print(f"\tAverage: {average}")
print(f"\tRemark: {get_remark(average)}")
