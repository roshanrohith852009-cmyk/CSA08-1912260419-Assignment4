
from datetime import datetime


class AttendanceSystem:

    def __init__(self):
        self.employees = {
            "EMP101": "Rohith",
            "EMP102": "Kailash",
            "EMP103": "Varun",
            "EMP104": "Nithin"
        }
        self.attendance = {}

    def verify_employee(self, employee_id):
        return employee_id in self.employees

    def mark_attendance(self, employee_id):

        if not self.verify_employee(employee_id):
            print("Employee not found!")
            return

        if employee_id in self.attendance:
            print("Attendance already marked!")
            return

        employee_name = self.employees[employee_id]
        current_time = datetime.now()

        self.attendance[employee_id] = current_time

        print("\nAttendance Marked Successfully!")
        print("Employee ID:", employee_id)
        print("Employee Name:", employee_name)
        print("Date:", current_time.strftime("%d-%m-%Y"))
        print("Time:", current_time.strftime("%H:%M:%S"))

    def display_attendance(self):

        print("\nATTENDANCE REPORT")
        print("--------------------------")

        if not self.attendance:
            print("No attendance records found.")
            return

        for employee_id, time in self.attendance.items():
            print(
                employee_id,
                self.employees[employee_id],
                time.strftime("%d-%m-%Y %H:%M:%S")
            )


def main():

    system = AttendanceSystem()

    while True:
        print("\n===== ATTENDANCE SYSTEM =====")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee_id = input("Enter Employee ID: ").strip().upper()
            system.mark_attendance(employee_id)

        elif choice == "2":
            system.display_attendance()

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
