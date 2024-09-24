class Book:
    number_of_copies_available = 1
    def __init__(self,title, author, year, available):
        self.title = title
        self.author = author
        self.year = year
        self.available = available


    @classmethod
    def update_books(cls):
        cls.number_of_copies_available += 1
        print(f"Total number of copies available: {cls.number_of_copies_available}")


    def details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nAvailable: {self.available}")
        
    def borrow_book(self, title):
        if self.available == True:
            self.available = False
            print("This book has been borrowed.")
            
    def return_book(self, title):
        if self.available == False:
            self.available = True
            print("This book has been returned.")

    @staticmethod
    def get_book_recommendation():
        print("You might also like: 'The Hunger Games")
    @staticmethod
    def quote():
        print("Books are man' best friends!")
            
book1 = Book("Harry Potter", "J.K. Rowling", 1997, True)
book2 = Book("Lord of the Rings", "John Ronald Reuel Tolkien", 1954, True)

book1.details()
book1.borrow_book("Harry Potter")
book1.update_books()

book1.return_book("Harry Potter")
book1.update_books()

Book.get_book_recommendation()
Book.quote()