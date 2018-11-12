from User import User


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []  # all users start with 0 input

    def get_title(self, title):
        return self.title

    def get_isbn(self, isbn):
        return self.isbn

    def set_isbn(self, isbn):
        print("This book's ISBN has been updated.")

    def add_rating(self, rating):
        if rating and (0 <= rating) and (rating <= 4):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if isinstance(other_book, Book):
            return self.book == other_book
        return False

    def get_average_rating(self):  
        average = 0
        sum = 0
        for val in self.ratings:
            sum += val
        
        average = sum / len(self.ratings)  # iterates through values in self.ratings of Book()
        return average

    def __hash__(self):
        return hash((self.title, self.isbn))  # this method makes Book hashable
    
    def __repr__(self):
        return "{}".format(self.title)
