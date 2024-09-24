class Book:
    # number_of_cars = 0
    def __init__(self,title, author, year, available):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    # @classmethod
    # def get_number_of_cars(cls):
    #
        
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
            
book1 = Book("Harry Potter", "J.K. Rowling", 1997, True)
book2 = Book("Lord of the Rings", "John Ronald Reuel Tolkien", 1954, True)

book1.details()
book1.borrow_book("Harry Potter")
book1.return_book("Harry Potter")

    