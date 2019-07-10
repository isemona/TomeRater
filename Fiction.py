from Book import Book as Parent 

class Fiction(Parent):
    def __init__(self, title, isbn, author): 
      super().__init__(title, isbn)
      self.author = author

    def get_author(self):
      return self.author

    def __repr__(self):
    	return "{title} by {author}".format(title = self.title, author = self.author)
    