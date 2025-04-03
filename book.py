class Book:
  def _init_(self,title,author,genre,Isbn,year):

    self.title = title
    self.author = author
    self.genre = genre
    self.Isbn = Isbn
    self.year = year

  def _str_(self):
    return f"Title:{self.title}, Author:{self.author}, Genre:{self.genre}, Isbn:{self.Isbn}, Year:{self.year}"