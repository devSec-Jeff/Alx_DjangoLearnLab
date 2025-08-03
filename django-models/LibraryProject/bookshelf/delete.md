"""
Delete the book you created and confirm deletion by trying to retrieve all books again
Output: (1, {'bookshelf.Book':1})
"""
from bookshelf.models import Book # I don't know why the auto-checker needs this line


book = Book.objects.get(id=1)
book.delete()

# Confirm deletion by trying to retrieve all books again

Book.objects.all().values()
