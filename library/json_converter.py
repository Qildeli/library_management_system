import json
from pathlib import Path


def save_to_json(library, data_dir):
    """Save the library's data to JSON files in directories."""
    # # Create a Path object for the data directory
    # data_directory = Path(data_dir)
    #
    # # Ensure the data directory exists
    # data_directory.mkdir(parents=True, exist_ok=True)

    # Define the file paths
    books_path = Path(data_dir) / 'books.json'
    borrowers_path = Path(data_dir) / 'borrowers.json'
    transactions_path = Path(data_dir) / 'transactions.json'

    # Save books
    with open(books_path, 'w') as json_file:
        books_data = {book_id: book.to_dict() for book_id, book in library.books.items()}
        json.dump(books_data, json_file, indent=4)

    # Save borrowers
    with open(borrowers_path, 'w') as json_file:
        borrowers_data = {borrower_id: borrower.to_dict() for borrower_id, borrower in library.borrowers.items()}
        json.dump(borrowers_data, json_file, indent=4)

    # Save transactions
    with open(transactions_path, 'w') as json_file:
        transactions_data = {transaction_id: transaction.to_dic()
                             for transaction_id, transaction in library.transactions.items()}
        json.dump(transactions_data, json_file, indent=4)
