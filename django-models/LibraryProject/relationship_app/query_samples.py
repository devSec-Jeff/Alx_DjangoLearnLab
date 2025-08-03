# Query all books by a specific author

author = input("Enter the author name:")
books_by_author = Book.objects.all().filter(name=author)


#List all Books in a Library
books_in_library = Library.objects.all().values()

#Retrieve the librarian for a Library
librarian = Librarian.objects.get(id=1)
