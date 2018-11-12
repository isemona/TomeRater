# import Book - don't import book here Book is not a module it is a class

from Book import Book as Parent # whyyy

class Fiction(Parent):
    def __init__(self, title, isbn, author): # what about rating?
      Parent.__init__(self, title, isbn)
      self.author = author

    def get_author(self, author):
      return self.author

    def __repr__(self):
    	return "{title} by {author}".format(title = self.title, author = self.author)
    