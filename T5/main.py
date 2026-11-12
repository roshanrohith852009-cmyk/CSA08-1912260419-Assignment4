
import calculator
from utilities.file_handler import save_result, read_results


def main():

    while True:
        print("\n===== CALCULATOR SYSTEM =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. View Saved Results")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "6":
            print("Thank you!")
            break

        if choice == "5":
            read_results()
            continue

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice!")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                result = calculator.add(a, b)
            elif choice == "2":
                result = calculator.subtract(a, b)
            elif choice == "3":
                result = calculator.multiply(a, b)
            else:
                result = calculator.divide(a, b)

            print("Result:", result)
            save_result(result)

        except ValueError:
            print("Please enter valid numbers.")

        except ZeroDivisionError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
