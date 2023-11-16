import uuid


class Book:
    """Add new books with details such as title, author, ISBN, genre, etc."""
    def __init__(self, title, author, isbn, genre):
        self.book_id = uuid.uuid4()
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre

    def update_book_details(self, title=None, author=None, isbn=None, genre=None):
        if title: self.title = title
        if author: self.author = author
        if isbn: self.isbn = isbn
        if genre: self.genre = genre

    def to_dict(self):
        return {
            'id': self.book_id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'genre': self.genre
        }
