from book import Book
from library import Library

def display_menu():
  print("\n--- Library Management System---")
  print("1. Add a new book")
  print("2. View all books")
  print("3. Search for a book by title")
  print("4. Update a book")
  print("5. Remove a book")
  print("6. Exit")

def add_book_interactive(library):
  print("\n Add a new book:")
  title = input ("Enter the title:")
  author = input ("Enter the author:")
  genre = input ("enter the genre:")
  year = input("enter the year:")
  ISBN = input ("Enter the ISBN:")

  from book import Book
  new_book =Book (title,author, genre, year, ISBN)
  library.add_books(new_book)

def search_book_interactive(library):
  title = input("\n Enter the title to search:")
  library.search_books_by_title(title)


def update_book_interactive(library):
  ISBN = input("\n Enter the ISBN of the book to update:")
  new_title = input("Enter the new title (leave blank to keep current):")
  new_author = input ("Enter the author (leave blank to keep current):")
  new_ISBN =  input ("enter the new ISBN (leave blank to keep current):")

  library.__update__(ISBN, new_ISBN, new_title, new_author)

def remove_book_interactive(library):
  ISBN = input ("\n enter the ISBN of the book to remove:")

  library.__remove__(ISBN)

def main():
  library = Library()

  while True:
    display_menu()
    choice = input ("enter your choice (1-6):")
    if choice == "1":
      add_book_interactive(Library)
    elif choice == "2":
      Library.display_all_books()
    elif choice == "3":
      search_book_interactive(Library)
    elif choice == "4":
      update_book_interactive(Library)
    elif choice == "5":
      remove_book_interactive(Library)
    elif choice == "6":
      print("\n Exiting the program. Goodbye!")
      break
    else:
      print("\nInvalid choice. please try again")

if __name__=="__main__":
    main()     



