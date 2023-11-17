import unittest
from library.borrower import Borrower


class TestUpdateBorrowerDetails(unittest.TestCase):
    def setUp(self):
        self.borrower = Borrower('Mamuka', 'mamuka@email.com')

    def test_update_borrower_details(self):
        self.borrower.update_borrower_details(name='Vigaca', contact='vigaca@email.com')
        self.assertEqual(self.borrower.name, 'Vigaca')
        self.assertEqual(self.borrower.contact, 'vigaca@email.com')


if __name__ == '__main__':
    unittest.main()