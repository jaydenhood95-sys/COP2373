import csv


def create_grades_file():
    """Create the grades.csv file and enter student grades."""

    number_of_students = int(input("How many students do you want to enter? "))

    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        for number in range(number_of_students):
            print(f"\nStudent {number + 1}")

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            writer.writerow([first_name, last_name, exam1, exam2, exam3])


def main():
    """Run the program."""
    create_grades_file()


if __name__ == "__main__":
    main()
