from datetime import date
from .json_converter import save_to_file, load_from_file
from .transaction import Transaction


class Library:
    """Library to add, remove and search books and borrowers.json.
       Record returned books and check overdue books."""

    def __init__(self):
        # import data
        self.books = load_from_file('data/books.json')
        self.borrowers = load_from_file('data/borrowers.json')
        self.transactions = load_from_file('data/transactions.json')

    def add_book(self, book):
        self.books[book.id] = book.to_dict()
        save_to_file(self.books, 'data/books.json')

    def remove_book(self, book_id):
        if book_id in self.books:
            raise ValueError(f'Book {book_id} is not found.')
        del self.books[book_id]
        save_to_file(self.books, 'data/books.json')

    def register_borrower(self, borrower):
        self.borrowers[borrower.id] = borrower.to_dict()
        save_to_file(self.borrowers, 'data/borrowers.json')

    def remove_borrower(self, borrower_id):
        if borrower_id not in self.borrowers:
            raise ValueError(f'Borrower {borrower_id} is not found.')
        del self.borrowers[borrower_id]
        save_to_file(self.borrowers, 'data/borrowers.json')

    def checkout_book(self, borrower_id, book_id):
        """Record each transaction."""
        # Create a new Transaction instance
        new_transaction = Transaction(borrower_id, book_id)
        # Add the transaction to the transactions dictionary using the transaction_id
        self.transactions[new_transaction.transaction_id] = new_transaction.to_dict()
        save_to_file(self.transactions, 'data/transactions.json')

    def returned_book(self, transaction_id):
        """Mark transaction as returned."""
        if transaction_id not in self.transactions:
            raise ValueError(f'Transaction {transaction_id} is not found.')

        # Create Transaction instance
        transaction_data = self.transactions[transaction_id]
        transaction = Transaction(transaction_data['borrower_id'], transaction_data['book_id'])
        # Use the Transaction method to mark it as returned
        transaction.mark_as_returned()
        # Update transactions dictionary with the new state of the transaction
        self.transactions[transaction_id] = transaction.to_dict()
        save_to_file(self.transactions, 'data/transactions.json')

    def check_overdue_books(self):
        overdue_transactions = {}  # Hold transactions that are overdue

        for transaction_id, transaction in self.transactions.items():
            if transaction.return_date is None and transaction.due_date < date.today():
                overdue_transactions[transaction_id] = transaction

        return overdue_transactions

    def search_books(self, keyword):
        # Search for books by title, author, genre, or ISBN.
        pass

    def search_borrowers(self, keyword):
        # Search for borrowers.json by name or contact information.
        pass
