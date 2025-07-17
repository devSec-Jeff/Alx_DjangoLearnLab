"""
Create a Book instance
Output: <Book Object (1)>
"""
Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
"""
Retrieve and display all attributes of the books created
Output: <QuerySet [{'title':'1984', 'author':'George Orwell', 'publicaton_year':1949}]>
"""
Book.objects.all().values('title','author','publication_year')
"""
Update the title of '1984' to 'Nineteen Eighty-Four'
Output: 1
"""

Book.objects.filter(title='1984').update(title='Nineteen Eighty-Four')
"""
Delete the book you created and confirm deletion by trying to retrieve all books again
Output: (1, {'bookshelf.Book':1})
"""
Book.objects.get(title='Nineteen Eighty-Four').delete()

# Confirm deletion by trying to retrieve all the books again
Book.objects.all().values('title', 'author','publication_year')
