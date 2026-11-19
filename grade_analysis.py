import numpy as np


def load_data(filename):
    # Load the grades from the CSV file.
    data = np.genfromtxt(filename, delimiter=",", skip_header=1,
                          usecols=(2, 3, 4))
    return data


def display_first_rows(data):
    # Display the first five rows of the grade data.
    print("First Few Rows of the Dataset")
    print("-----------------------------")
    print(data[:5])


def calculate_statistics(data):
    # Calculate statistics for each exam.
    print("\nStatistics for Each Exam")
    print("------------------------")

    for exam_number in range(data.shape[1]):
        exam = data[:, exam_number]

        print(f"\nExam {exam_number + 1}")
        print(f"Mean: {np.mean(exam):.2f}")
        print(f"Median: {np.median(exam):.2f}")
        print(f"Standard Deviation: {np.std(exam):.2f}")
        print(f"Minimum: {np.min(exam):.2f}")
        print(f"Maximum: {np.max(exam):.2f}")

    # Combine all exam grades into one array.
    all_grades = data.flatten()

    # Calculate overall statistics.
    print("\nOverall Statistics")
    print("------------------")
    print(f"Mean: {np.mean(all_grades):.2f}")
    print(f"Median: {np.median(all_grades):.2f}")
    print(f"Standard Deviation: {np.std(all_grades):.2f}")
    print(f"Minimum: {np.min(all_grades):.2f}")
    print(f"Maximum: {np.max(all_grades):.2f}")


def calculate_pass_fail(data):
    # Calculate the number of students who passed and failed each exam.
    print("\nPass/Fail Results")
    print("-----------------")

    total_passed = 0
    total_grades = data.size

    for exam_number in range(data.shape[1]):
        exam = data[:, exam_number]

        passed = np.sum(exam >= 60)
        failed = np.sum(exam < 60)

        total_passed += passed

        print(f"\nExam {exam_number + 1}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")

    # Calculate the overall pass percentage.
    pass_percentage = (total_passed / total_grades) * 100

    print("\nOverall Pass Percentage")
    print("-----------------------")
    print(f"{pass_percentage:.2f}%")


def main():
    # Name of the CSV file.
    filename = "grades.csv"

    # Load the grade data.
    data = load_data(filename)

    # Display the first few rows.
    display_first_rows(data)

    # Calculate and display statistics.
    calculate_statistics(data)

    # Calculate and display pass/fail results.
    calculate_pass_fail(data)


# Run the main function.
if __name__ == "__main__":
    main()
