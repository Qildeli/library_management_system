import unittest
from library.book import Book


class TestUpdateBookDetails(unittest.TestCase):
    def setUp(self):
        self.book = Book('The Stranger', 'Albert Camus', '210987148', 'Absurdist fiction')

    def test_update_book_details(self):
        self.book.update_book_details(title='1984', author='George Orwell',
                                      isbn='134791233', genre='Dystopian')
        self.assertEqual(self.book.title, '1984')
        self.assertEqual(self.book.author, 'George Orwell')
        self.assertEqual(self.book.isbn, '134791233')
        self.assertEqual(self.book.genre, 'Dystopian')


if __name__ == '__main__':
    unittest.main()
