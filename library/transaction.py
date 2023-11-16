import uuid
from datetime import date, timedelta


class Transaction:
    """Transaction history with details such as book, borrower, due date, return date."""
    def __init__(self, borrower_id, book_id):
        self.transaction_id = uuid.uuid4()
        self.borrower_id = borrower_id
        self.book_id = book_id
        self.checkout_date = date.today()  # Date when book is borrowed
        self.due_date = self.checkout_date + timedelta(14)  # 2-week book loan period
        self.return_date = None
        self.status = 'checked_out'

    def mark_as_returned(self):
        self.return_date = date.today()
        self.status = 'returned'
