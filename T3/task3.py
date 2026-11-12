
class InvalidAgeError(Exception):
    pass


class InvalidMarksError(Exception):
    pass


def validate_student(name, age, marks):

    if not name.strip():
        raise ValueError("Student name cannot be empty")

    if age < 17 or age > 100:
        raise InvalidAgeError("Age must be between 17 and 100")

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")

    return True


def main():

    print("STUDENT VALIDATION SYSTEM")
    print("-------------------------")

    try:
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        validate_student(name, age, marks)

        print("\nStudent Details")
        print("Name:", name)
        print("Age:", age)
        print("Marks:", marks)
        print("Status: Valid Student Record")

    except InvalidAgeError as error:
        print("Age Error:", error)

    except InvalidMarksError as error:
        print("Marks Error:", error)

    except ValueError as error:
        print("Input Error:", error)


if __name__ == "__main__":
    main()
