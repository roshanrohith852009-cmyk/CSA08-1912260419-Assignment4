
import csv
import os

from validation import (
    validate_name,
    validate_email,
    validate_event
)


class FestRegistration:

    def __init__(self):

        self.filename = "data/registrations.csv"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Registration ID",
                    "Name",
                    "Email",
                    "Event"
                ])

    def register_student(self, reg_id, name, email, event):

        if not validate_name(name):
            print("Invalid student name!")
            return False

        if not validate_email(email):
            print("Invalid email address!")
            return False

        if not validate_event(event):
            print("Invalid event selection!")
            return False

        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([reg_id, name, email, event])

        print("\nRegistration Successful!")
        print("Registration ID:", reg_id)
        print("Student Name:", name)
        print("Event:", event)

        return True

    def display_registrations(self):

        print("\nCOLLEGE FEST REGISTRATION REPORT")
        print("--------------------------------")

        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.reader(file)

                for row in reader:
                    print(" | ".join(row))

        except FileNotFoundError:
            print("Registration file not found.")
