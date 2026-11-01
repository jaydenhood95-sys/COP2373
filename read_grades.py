import csv


def read_grades_file():
    """Read grades.csv and display the student grades."""

    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)

        header = next(reader)

        print(f"{header[0]:<15}{header[1]:<15}{header[2]:<10}"
              f"{header[3]:<10}{header[4]:<10}")
        print("-" * 60)

        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}"
                  f"{row[3]:<10}{row[4]:<10}")


def main():
    """Run the program."""
    read_grades_file()


if __name__ == "__main__":
    main()
