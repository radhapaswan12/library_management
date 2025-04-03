import book
import json
import os

class Library:
  def __init__(self):
    self.books=[]

  def add_books(self,book):
    self.books.append(book)
    print(f"the book '{book.title}' is added to the library")

  def display_all_books(self):
    if self.books:
      print("all the books in the library")
      for book in self.books:
        print(book)
    else:
      print("this library is empty!")

  def search_books_by_title(self,title):
    search_book=[book for book in self.books if title.lower() in title. lower()]
    if search_book:
      print(f"found{len(search_book)} books by {'title'}")  
    else:
      print(f"no books by the title '{title}' was found")
 
  def __update__(self,ISBN, new_ISBN=None, new_title=None,new_author=None):
    for book in self.books:
      if ISBN == ISBN:
        if new_title:
          book.title=new_title
        if new_ISBN:
          book.ISBN=new_ISBN
        if new_author:
          book.author=new_author
          print(f"Book with isbn '{ISBN}' updated successfulley!")
        else:
          print(f"cannot update books with isbn '{ISBN}' ")  

  def __remove__self(self,ISBN):
    for book in self.books:
      if book.ISBN == ISBN:
        self.books.remove(book)
        print (f"book with isbn '{ISBN}' removed fromm the library") 
        return
      print (f"book with isbn '{ISBN}' failed to remove")       

  def save_books(self):
    with open ("books.json",'w') as file:
      json.dump (self.books, file,indent = 4)

  def load_books(self):
    if os.path.exists("books.json"):
      with open ("books.json",'r') as f:
        try:
          return json.loads(f)
        except json.JSONDecodeError:
          print("error empyt list")
          return[]
    return[]          