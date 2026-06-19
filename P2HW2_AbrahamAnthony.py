 # Your Name: Antony Abraham
 # Date: 18 JUNE 2026
 # Assignment Name: P2HW2
 # A brief description of the project: Calculates and displays the lowest grade, highest grade, sum of grades, and average grade for a list of grades entered by the user. 
 # The program prompts the user to enter grades for six modules, stores them in a list, and then uses built-in functions to calculate and display the required information in a formatted manner.


# Instructions:

# For this assignment, you are to design a program that does the following:

#Asks the user to enter grades for following tests. Each grade is to be requested in a separate statement
#Module 1
#Module 2
#Module 3
#Module 4
#Module 5
#Module 6
#The program should store the grades entered in a list. Give the list created a descriptive name

#Display the following: (10 points each)
#The lowest grade in the list
#The highest grade in the list
#Sum of grades
#The grades' average


#Grades Section
#--------------

# Collectthe grades for each module and store them in a variable.  This will allow users to enter the grades for each module when prompted. 
module1_grade = float(input("\nEnter grade for Module 1: "))
module2_grade = float(input("Enter grade for Module 2: "))
module3_grade = float(input("Enter grade for Module 3: "))
module4_grade = float(input("Enter grade for Module 4: "))
module5_grade = float(input("Enter grade for Module 5: "))
module6_grade = float(input("Enter grade for Module 6: "))

# create a list to store the grades

lsGrades = [module1_grade, module2_grade, module3_grade, module4_grade, module5_grade, module6_grade] # Create a list to store the grades
# print("\nGrades:", lsGrades) # Print the list of grades

# Results Section: 
#-----------------

sym = '-'
line = sym * 15
footer = sym * 37

# Use the print statement and available functions to find the lowest grade (min() function), highest grade (max() function), 
# sum of grades (sum() function), and average grade (sum() function divided by len() function), and display the results in the required format.

print(f"\n{line}Results{line}") # Print a line of dashes, followed by the title "Results", and another line of dashes to create a header for the results section.

print(f'{"Lowest Grade:":<20} {min(lsGrades)}') # Print the lowest grade in the list
print(f'{"Highest Grade:":<20} {max(lsGrades)}') # Print the highest grade in the list
print(f'{"Sum of Grades:":<20} {sum(lsGrades)}') # Print the sum of grades
print(f'{"Average Grade:":<20} {sum(lsGrades)/len(lsGrades):.2f}') # Print the grades' average with two decimal positions only

print(f'{footer}\n') # Print a line of dashes to create a footer for the results section.
