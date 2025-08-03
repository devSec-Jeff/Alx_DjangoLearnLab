"""
Update the title of '1984' to 'Nineteen Eighty-Four'
Output: 1
"""

# Book.objects.filter(title='1984').update(title='Nineteen Eighty-Four')

book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()
