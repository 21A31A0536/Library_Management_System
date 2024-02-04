class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self.isbn

    def is_borrowed(self):
        return self.borrowed

    def borrow(self):
        if self.borrowed:
            return False
        else:
            self.borrowed = True
            return True

    def return_book(self):
        if not self.borrowed:
            return False
        else:
            self.borrowed = False
            return True
            
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_available_books(self):
        available_books = []
        for book in self.books:
            if not book.is_borrowed():
                available_books.append(book)
        return available_books
                
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()

book_name = input("Enter Book Name : ")
book_author = input("\nEnter Author Name : ")
book_isbn = input("\nEnter Book ISBN : ")
book = Book(book_name,book_author,book_isbn)

library = Library()
library.add_book(book)

member_name = input("\nEnter Member Name : ")
member = Member(member_name)

book_to_borrow = input("\nEnter Name of the Book to Borrow : ")
book_to_return = input("\nEnter Name of the Book to Return : ")

borrowed_book = None
for book in library.books:
    if book.get_title() == book_to_borrow:
        member.borrow_book(book)
        break
    if borrowed_book:
        member.borrow_book(borrowed_book)
    else:
        print("\nBook Not Found or Already Borrowed")
    
returned_book = None
for book in member.borrowed_books:
    if book.get_title() == book_to_return:
        member.return_book(book)
        break
    if returned_book:
        member.return_book(returned_book)
        
available_books = library.get_available_books()
if available_books:
    print("\nAvailable Books: ")
    for book in available_books:
        print(book.get_title())
else:
    print("\nNO Available Books")
         
    

