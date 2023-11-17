import unittest
from unittest.mock import patch
from library.library import Library


class TestLibraryLoadData(unittest.TestCase):
    def setUp(self):
        self.mock_books_data = {'book1':
            {
                'title': 'The Stranger',
                'author': 'Albert Camus',
                'isbn': '341987',
                'genre': 'Absurdist fiction'
            }
        }
        self.mock_borrowers_data = {'borrower1':
            {
                'name': 'Mamuka',
                'contact': 'mamuka@email.com'
            }
        }
        self.mock_transactions_data = {'transaction1':
            {
                'borrower_id': 'borrower1',
                'book_id': 'book1',
                'checkout_date': '2023-07-01',
                'due_date': '2023-07-15',
                'return_date': None,
                'status': 'checked_out'
            }
        }

    @patch('library.library.load_from_file')
    def test_initialization(self, mock_load):
        mock_load.side_effect = [self.mock_books_data, self.mock_borrowers_data, self.mock_transactions_data]

        library_instance = Library()

        self.assertEqual(library_instance.books, self.mock_books_data)
        self.assertEqual(library_instance.borrowers, self.mock_borrowers_data)
        self.assertEqual(library_instance.transactions, self.mock_transactions_data)


if __name__ == '__main__':
    unittest.main()
