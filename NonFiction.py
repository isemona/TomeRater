from Book import Book as Parent

class NonFiction(Parent): 
    def __init__(self, title, isbn, subject, level): 
      super().__init__(title, isbn)
      self.subject = subject
      self.level = level

    def get_subject(self):
      return self.subject

    def get_level(self):
      return self.level

    def __repr__(self):
    	return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)