
import logging
from datetime import datetime

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Library:

    def __init__(self):
        self.books = {
            101: "Python Programming",
            102: "Data Structures",
            103: "Database Management",
            104: "Computer Networks"
        }
        self.issued_books = {}

    def display_books(self):

        print("\nAVAILABLE BOOKS")
        print("----------------")

        for book_id, book_name in self.books.items():
            if book_id not in self.issued_books:
                print(book_id, "-", book_name)

    def issue_book(self, book_id):

        if book_id not in self.books:
            logging.warning("Invalid book ID: %s", book_id)
            print("Book not found!")
            return

        if book_id in self.issued_books:
            logging.warning("Book already issued: %s", book_id)
            print("Book already issued!")
            return

        self.issued_books[book_id] = datetime.now()
        logging.info("Book issued: %s", self.books[book_id])
        print("Book issued successfully!")

    def return_book(self, book_id):

        if book_id not in self.issued_books:
            logging.warning("Invalid return attempt: %s", book_id)
            print("Book was not issued!")
            return

        del self.issued_books[book_id]
        logging.info("Book returned: %s", self.books[book_id])
        print("Book returned successfully!")


def main():

    library = Library()

    while True:
        print("\n===== LIBRARY SYSTEM =====")
        print("1. Display Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                library.display_books()

            elif choice == "2":
                book_id = int(input("Enter Book ID: "))
                library.issue_book(book_id)

            elif choice == "3":
                book_id = int(input("Enter Book ID: "))
                library.return_book(book_id)

            elif choice == "4":
                print("Exiting Library System.")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            logging.error("Invalid input entered by user")
            print("Please enter a valid numeric Book ID.")


if __name__ == "__main__":
    main()
