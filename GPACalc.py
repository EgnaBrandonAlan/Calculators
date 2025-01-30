# Introduce the user to the program
print("This is an Unweighted Semester-Based Cumulative GPA Calculator.")
print("It uses the amount of semesters you have taken total and the grade received in each semester.")
print("You will also receive feedback on your GPA.")


# GPA Calculator function
"""
A function takes in parameters, which act as placeholders for values which will be passed into the function.
The parameters in this function are grade_points and semester_amount.
This function uses the grade points, which is a list, and semester amount to calculate your GPA.
"""
def calculate_GPA(grade_points, semester_amount):
    # Sum the grade point values and use the averaging formula
    total_points = sum(grade_points)
    GPA = total_points / semester_amount
    return GPA


# Converting letter grades to grade points function
def grade_point_conversion(letter_grades):
    # Dictionary of letter grades to grade points (4.0 Scale)
    """
    A dictionary corresponds one value to another, called key-value pairs.
    In this case, each letter is a key and the grade points are the value.
    """
    grade_points = {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "D-": 0.0,
        "F": 0.0
    }
    # Check if the inputted value is in the dictionary (not case sensitive) and return the point value
    """
    An if statement checks for a condition. In this case, we are checking for if the letter grade which
    has been input is part of our dictionary grade_points.
    The .upper() method makes the input uppercase regardless, making our code case insensitive.
    We then return the value of the grade point.
    """
    if letter_grades.upper() in grade_points:
        return grade_points[letter_grades.upper()]
    # Error handling for if a value is inputted which is not in the dictionary
    else:
        print("Error: Must be a valid letter grade (A, A-, B, ...)")


# Grade input function
def input_grades(semester_amount):
    semester_grade_points = []
    # Iterate through the length of the list to replace letters with points
    for i in range(1, semester_amount + 1):
        while True:
            # Prompt the user for a letter grade and convert it to grade points
            grade = input(f"What is your grade in semester number {i}? ")
            grade_point = grade_point_conversion(grade)
            # Forever loop breaks if the input is valid and prompts the user again if invalid
            if grade_point is not None:
                semester_grade_points.append(grade_point)
                break
    # Returns the grade points list
    return semester_grade_points


# Semester input function
def input_semesters():
    try:
        # Prompt the user for the amount of semesters taken
        semester_amount = int(input("How many total semesters have you taken? "))
        # Print an error and prompt the user again if an invalid input is given
        if semester_amount <= 0:
            raise ValueError
        return semester_amount
    except ValueError:
        print("Error: Must be a positive integer number")
        return input_semesters()


def main():

    # Fetch semester amount and grade points for GPA Calculation
    semester_amount = input_semesters()

    total_grade_points = input_grades(semester_amount)

    # Calculate and print the user's GPA rounded to 4 decimal places
    GPA = round(calculate_GPA(total_grade_points, semester_amount), 4)
    print("Your GPA is:", GPA)

    # Print feedback on the user's GPA
    if GPA >= 3.0:
        print("You have a remarkable GPA!")
    elif GPA >= 2.0:
        print("You have an average GPA.")
    else:
        print("Your GPA could use some improvement.")


# Run the program
main()
