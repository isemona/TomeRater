from Book import Book
from User import User
from Fiction import Fiction
from NonFiction import NonFiction

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title,isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, isbn, author)
	
    def create_non_fiction(self, title, subject, level, isbn):
        return NonFiction(title, subject, level, isbn)
	
    def add_book_to_user(self, book, email, rating=None):
        for key,user in self.users.items():
            if user.email == email:
                user.read_book(book,rating) 
                book.add_rating(rating) 
                if book not in self.books:
                    self.books[book] = 1
                else:
                    self.books[book] += 1
                return user # is equivalent to get, know what the method returns
        print("No user with email {email}!".format(email = email))
	
    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name,email)
        if user_books:
            for book in user_books:
                self.add_book_to_user(book,email)
    
    def print_catalog(self):
        for key in self.books: # singular object so call it key instead of keys
            print(key)

    def print_users(self):
        for user in self.users:
            print(user)
    
    def most_read_book(self):
        most_read = None
        most_read_count = 0
        for book,val in self.books.items():
            if val > most_read_count:
                most_read_count = val
                most_read = book # count how many times it has been read
        return most_read
    
    def highest_rated_book(self):
        rated_book = None
        highest_rating_count = 0
        for book in self.books:
            if book.get_average_rating() > highest_rating_count:
                highest_rating_count = book.get_average_rating()
                rated_book = book
        return rated_book

    def most_positive_user(self):
        positive_user = None
        highest_average_rating = 0
        for email,user in self.users.items():
            if user.get_average_rating() > highest_average_rating:
               highest_average_rating = user.get_average_rating()
               positive_user = user
        return positive_user