class LibraryBook:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already available in the library.")

    def details(self):
        status = "Available" if self.available else "Borrowed"

        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"ISBN   : {self.isbn}")
        print(f"Year   : {self.year}")
        print(f"Status : {status}")
        print("-" * 30)


# Creating the three books objects
book1 = LibraryBook(
    "Hanging Tree",
    "Ben Aaronovitch",
    "15791898999",
    2020
)

book2 = LibraryBook(
    "A Promised Land",
    "Barack Obama",
    "15179819161",
    2021
)

book3 = LibraryBook(
    "Dreams from the Future",
    "Isaac Benson",
    "5618675190",
    1967
)


# Testing Book 1
book1.details()
book1.borrow()
book1.details()
book1.return_book()
book1.details()

# Testing Book 2
book2.details()
book2.borrow()
book2.details()
book2.return_book()
book2.details()

# Testing Book 3
book3.details()
book3.borrow()
book3.details()
book3.return_book()
book3.details()