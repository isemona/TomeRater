from Book import Book as Parent

class NonFiction(Parent): 
    def __init__(self, title, subject, level, isbn): 
      Parent.__init__(self, title, isbn)
      self.subject = subject
      self.level = level

    def get_subject(self, subject):
      return self.subject

    def get_level(self, level):
      return self.level

    def __repr__(self):
    	return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)