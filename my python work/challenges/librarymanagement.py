""""
Challenge: Library Management System

Problem Statement:

Design a Library Management System using OOP principles where:

Users can borrow and return books.
A book can be available or already borrowed by someone else.
Maintain a record of borrowed books.
Ensure a book cannot be borrowed if it is already issued.

Requirements:

Create a Book class with attributes: title, author, and available.

Create a Library class with methods to:
Add books to the collection.
Display available books.
Borrow a book (mark it as unavailable if borrowed).
Return a book (mark it as available again).

"""""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Book is available by default

    def __str__(self):
        return f"'{self.title}' by {self.author} - {'Available' if self.available else 'Borrowed'}"

class Library:
    def __init__(self): # constructor.
        self.books = [] # list for books.

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.available:
                print(book)
        print()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"You borrowed '{book.title}'")
                return
        print("Sorry, book not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"You returned '{book.title}'")
                return
        print("Invalid return. Book was not borrowed.")

# Sample Execution
library = Library()
book=Book("salman","what matters")
print(book)
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")

library.display_books()
library.borrow_book("1984")
library.display_books()
library.return_book("1984")
library.display_books()
