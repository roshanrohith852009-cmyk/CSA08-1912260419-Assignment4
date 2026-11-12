
def calculate_average(marks):
    if not marks:
        raise ValueError("Marks list cannot be empty")
    return sum(marks) / len(marks)


def main():
    try:
        with open("T1/marks.txt", "r") as file:
            marks = [float(line.strip()) for line in file if line.strip()]

        if any(mark < 0 or mark > 100 for mark in marks):
            raise ValueError("Marks must be between 0 and 100")

        average = calculate_average(marks)

        print("STUDENT MARK ANALYSIS")
        print("---------------------")
        print("Number of subjects:", len(marks))
        print("Total marks:", sum(marks))
        print("Average marks:", round(average, 2))

        if average >= 90:
            print("Grade: A")
        elif average >= 75:
            print("Grade: B")
        elif average >= 50:
            print("Grade: C")
        else:
            print("Grade: D")

    except FileNotFoundError:
        print("Error: marks.txt file not found.")
    except ValueError as error:
        print("Invalid data:", error)


if __name__ == "__main__":
    main()
