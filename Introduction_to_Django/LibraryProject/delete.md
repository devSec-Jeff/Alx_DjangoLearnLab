"""
Delete the book you created and confirm deletion by trying to retrieve all books again
Output: (1, {'bookshelf.Book':1})
"""
Book.objects.get(title='Nineteen Eighty-Four').delete()

# Confirm deletion by trying to retrieve all the books again
Book.objects.all().values('title', 'author','publication_year')
