# Books
# - Remove books from the library.
# - Search for books by title, author, genre, or ISBN.

# Borrowers
# - Remove borrowers from the system.
# - Search for borrowers by name or contact information.

# Transaction
# - Record the return of books.
# - Check for overdue books.

from library.transaction import Transaction


class Library:
    """Library to add, remove and search books and borrowers.
        Record returned books and check overdue books"""
    def __init__(self):
        self.books = {}
        self.borrowers = {}
        self.transactions = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]

    def register_borrower(self, borrower):
        self.borrowers[borrower.borrower_id] = borrower

    def remove_borrower(self, borrower_id):
        if borrower_id in self.borrowers:
            del self.borrowers[borrower_id]

    def checkout_book(self, borrower_id, book_id):
        """Record each transaction"""
        transaction = Transaction(borrower_id, book_id)
        self.transactions[transaction.transaction_id] = transaction

    def returned_book(self, transaction_id):
        transaction = self.transactions[transaction_id]  # Get the transaction from transactions dictionary
        if transaction not in self.transactions:
            raise ValueError(f'{transaction} is not found')
        transaction.mark_as_returned()  # Mark transaction as returned

    def search_books(self, keyword):
        pass

    def check_overdue_books(self):
        pass

    def search_borrowers(self, keyword):
        pass
