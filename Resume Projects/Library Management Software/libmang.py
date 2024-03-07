"""
Dattesh Sukhadia
E-mail: sukhadid@mcmaster.ca

Project - Advanced Library management software

Our Advanced Library Management System is a feature-rich software program
designed to improve user experience, expedite library operations,
and streamlined book management procedures.
For both administrators and users, it provides an advanced platform
that guarantees effective book tracking, effortless access to library resources,
and smooth interaction with the library's collection.


Key Features:

Intuitive User Interface:
The system boasts a user-friendly interface that facilitates effortless navigation
and enhances the overall user experience for both administrators and library patrons

Extensive Book Collection Management:
With our system, administrators can efficiently manage the library's book collection,
including adding new books, removing outdated resources, and updating book details with ease.

Advanced Book Tracking:
Users can easily track their reading progress with features such as bookmarking, last-page tracking,
and quick access to previously read pages, ensuring a seamless reading experience across multiple sessions.

Role-Based Access Control:
The system incorporates role-based access control, allowing administrators to perform privileged operations
such as adding and removing books, while users can access and interact with the library's collection according to their permissions.

Centralized Data Management:
Our system employs a centralized database architecture to store and manage library data securely,
ensuring data integrity and easy retrieval of information whenever needed.

Robust Search Functionality:
Users can quickly search for books based on various criteria
such as title, author, genre, or ISBN, enabling them to find relevant resources efficiently.

Customizable Settings:
The system offers customizable settings that allow administrators to tailor
the software according to the specific requirements and preferences of their library,
ensuring flexibility and adaptability.

Comprehensive Reporting:
Administrators can generate detailed reports on library activities,
including book circulation, user borrowing patterns, and popular book titles,
providing valuable insights for decision-making and resource allocation.

"""

class Book:
    def __init__(self, book_id, title, content):
        self.book_id = book_id
        self.title = title
        self.content = content
        self.lp = 0             #displays the last page of an active book

    def display_page(self):
        return self.content[self.lp]
    def turn_page(self):
        self.lp = self.lp + 1       #increments the current page by 1
        return self.display_page()

class Library:
    def __init__(self):
        self.collection = dict()    #collection of books in the library; currently an empty dictionary
        self.active_book = None
        self.id_counter = 0

    def add_to_collection(self, title, content):
        new_book = Book(self.id_counter, title, content)
        self.collection[new_book.id] = new_book             #add new book to collection
        self.id_counter = self.id_counter + 1

    def remove_from_collection(self, book_id):
        if book_id in self.collection:
            del self.collection[book_id]        #remove books from collection based on their id
        return print("Book not found in the collection!")


    def set_active_book(self, book_id):
        if book_id in self.collection:
            self.active_book = self.collection[book_id]
            print(f"'{self.active_book.title}' is now active")
        return print("Book not found in collection!")

    def display_active_book_page(self):
        if self.active_book:
            return self.active_book.display_page()
        return print("No active book selected!")

    def turn_page(self):
        return self.collection[self.active_book].turn_page()

class User:
    def __init__(self, library):
        self.library = library

    def view_books(self):
        for book_id, book in self.library.collection.items():
            print(f"ID: {book_id}, Title: {book.title}")

    def view_active_book_page(self):
        return self.library.display_active_book_page()

class Admin(User):
    def __init__(self, library):
        super(Admin, self).__init__(library)

    def add_book(self, title, content):
        self.library.add_to_collection(title, content)

    def remove_book(self, book_id):
        self.library.remove_from_collection(book_id)

    def set_active_book(self, book_id):
        self.library.set_active_book(book_id)


