import uuid


class Borrower:
    """Register new borrowers.json with their details like name, contact"""
    def __init__(self, name, contact):
        self.borrower_id = uuid.uuid4()
        self.name = name
        self.contact = contact

    def update_borrower_details(self, name=None, contact=None):
        if name: self.name = name
        if contact: self.contact = contact
