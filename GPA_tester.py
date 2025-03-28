"""
Billy Parrish
GPA_Tester
Description: This app accepts student names and GPAs and tests if the student qualifies for either the Dean's List or the Honor Roll.
"""

def main():
    while True:
        # Ask for and accept a student's last name
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
        
        # Quit processing student records if the last name entered is 'ZZZ'
        if last_name == 'ZZZ':
            break
        
        # Ask for and accept a student's first name
        first_name = input("Enter student's first name: ")
        
        # Ask for and accept the student's GPA as a float
        gpa = float(input("Enter student's GPA: "))
        
        # Test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        
        # Test if the student's GPA is 3.25 or greater and, if so, print a message saying that the student has made the Honor Roll
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        
        else:
            print(f"{first_name} {last_name} has not qualified for the Dean's List or Honor Roll.")

# Test the app using at least five students
if __name__ == "__main__":
    main()
