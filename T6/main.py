
from registration import FestRegistration


def main():

    fest = FestRegistration()
    registration_id = 1001

    while True:
        print("\n===== COLLEGE FEST REGISTRATION =====")
        print("1. Register Student")
        print("2. View Registrations")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            name = input("Enter student name: ")
            email = input("Enter email address: ")

            print("\nAvailable Events:")
            print("1. Coding")
            print("2. Dance")
            print("3. Singing")
            print("4. Quiz")
            print("5. Photography")

            event_choice = input("Select event (1-5): ")

            events = {
                "1": "Coding",
                "2": "Dance",
                "3": "Singing",
                "4": "Quiz",
                "5": "Photography"
            }

            event = events.get(event_choice, "")

            success = fest.register_student(
                registration_id,
                name,
                email,
                event
            )

            if success:
                registration_id += 1

        elif choice == "2":
            fest.display_registrations()

        elif choice == "3":
            print("Thank you for using the registration system!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
