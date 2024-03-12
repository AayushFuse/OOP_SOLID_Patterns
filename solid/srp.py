"""
[Single-Responsibility Principle (SRP)] Implement a simple program to interact with the library catalog system. 
Create a Python class Book to represent a single book with attributes: Title, Author, ISBN, Genre, Availability (whether the book is available for borrowing or not). 
Create another Python class LibraryCatalog to manage the collection of books with following functionalities:
Add books by storing each book objects (Hint: Create an empty list in constructor and store book objects)
get book details and get all books from the list of objects
Lets say, we need a book borrowing process (what books are borrowed and what books are available for borrowing). 
Implement logics to integrate this requirement in the above system. 
Design the classes with a clear focus on adhering to the Single Responsibility Principle(SRP) 
which represents that "A module should be responsible to one, and only one, actor."
"""

class Book:
    def __init__(self,title,author,isbn,genre,is_available) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.is_available = is_available

    def __str__(self):
        return f"Book Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nGenre: {self.genre}\nAvailability: {self.is_available}"


class LibraryCatalog:
    def __init__(self) -> None:
        self.book_list=[]

    @property
    def books(self):
        return self.book_list

    @books.setter
    def books(self,book):
        if isinstance(book,Book):
            self.book_list.append(book)
        else:
            raise ValueError("Invalid Book Object")
        
    def get_book(self,isbn):
        for book in self.book_list:
            if book.isbn == isbn:
                return book
        return None
            
            
class BookBorrow:
    def __init__(self,catalog) -> None:
        self.__catalog = catalog
        self.available_books = [book for book in self.__catalog.books if book.is_available]
        self.borrowed_books = [book for book in self.__catalog.books if not book.is_available]
        
    def display_available_books(self):
        for book in self.available_books:
            print(book)
    
    def get_borrowed_books(self):
        for book in self.borrowed_books:
            print(book)
            
    def check_availability(self,isbn):
        book = self.__catalog.get_book(isbn)
        if book:
            if book in self.available_books:
                return True
            else: 
                return False
        else:
            return False
        
        
    
            
if __name__ == "__main__":
    book1 = Book("ZeroToOne","Peter Thiel","908x900","Business",False)
    book2 = Book("The Lean Startup","Eric Ries","908x901","Business",False)
    lc = LibraryCatalog()
    lc.books = book1
    lc.books = book2
    # print(lc.get_book("908x901"))
    b = BookBorrow(lc)
    # b.get_borrowed_books()
    print(b.check_availability("908x900"))

    # print([book for book in lc.books if not book.is_available])
