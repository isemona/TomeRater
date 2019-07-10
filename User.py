import Book 

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {} # all users start with 0 input

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("This users email has been updated to: {email}.".format(email = self.email))

    def __repr__(self):
        return "User {name}, email: {email}, books read: {number}".format(name = self.name, email = self.email, number = len(self.books))

    def __eq__(self, other_name):
    	if isinstance(other_name, User):
    		return self.name == other_name.name
    	return False

    # this part makes User and Books interact through TomeRater	
    def read_book(self, book, rating = None):
      self.books[book] = rating
    
    def get_average_rating(self): 
        average = sum(self.books.values())/len(self.books) # length of self.book dictionary
        return average