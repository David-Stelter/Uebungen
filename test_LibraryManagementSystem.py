import unittest
from unittest.mock import patch, call
import copy # For deepcopying dictionaries

# It's safer to import the module and access its members
import LibraryManagementSystem as lms

# Original state of the library's global variables for resetting in setUp
ORIGINAL_BOOKS = {
    "book1": 1,
    "book2": 3,
    "book3": 0
}
ORIGINAL_BOOKS_RENTED = {
    "book1": 2,
    "book2": 0,
    "book3": 3
}

@patch('time.sleep', return_value=None) # Patch time.sleep for all tests in this class
class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        # Deepcopy original states to lms.books and lms.books_rented before each test
        lms.books = copy.deepcopy(ORIGINAL_BOOKS)
        lms.books_rented = copy.deepcopy(ORIGINAL_BOOKS_RENTED)

    # 1. Tests for view_available_books()
    @patch('builtins.print')
    def test_view_multiple_copies(self, mock_print, mock_sleep):
        lms.books = {"bookA": 3, "bookB": 5}
        lms.view_available_books()
        expected_calls = [
            call("We have 3 copies of bookA available"),
            call("We have 5 copies of bookB available")
        ]
        # Check if all expected calls are present, regardless of order for dict items
        self.assertEqual(mock_print.call_count, len(expected_calls))
        for exp_call in expected_calls:
            self.assertIn(exp_call, mock_print.call_args_list)

    @patch('builtins.print')
    def test_view_one_copy(self, mock_print, mock_sleep):
        lms.books = {"bookC": 1}
        lms.view_available_books()
        mock_print.assert_called_once_with("We have 1 copy of bookC available")

    @patch('builtins.print')
    def test_view_no_books_available(self, mock_print, mock_sleep):
        lms.books = {"bookD": 0, "bookE": 0}
        lms.view_available_books()
        mock_print.assert_not_called() # Function only prints if element > 0

    @patch('builtins.print')
    def test_view_mixed_copies(self, mock_print, mock_sleep):
        lms.books = {"bookA": 2, "bookB": 1, "bookC": 0}
        lms.view_available_books()
        expected_calls = [
            call("We have 2 copies of bookA available"),
            call("We have 1 copy of bookB available")
        ]
        self.assertEqual(mock_print.call_count, len(expected_calls))
        for exp_call in expected_calls:
            self.assertIn(exp_call, mock_print.call_args_list)


    @patch('builtins.print')
    def test_view_empty_library(self, mock_print, mock_sleep):
        lms.books = {}
        lms.view_available_books()
        mock_print.assert_not_called()

    # 2. Tests for borrow_books()
    @patch('builtins.print')
    @patch('builtins.input')
    def test_borrow_available_book(self, mock_input, mock_print, mock_sleep):
        lms.books = {"book1": 2, "book2": 1}
        lms.books_rented = {"book1": 0, "book2": 0} # Ensure rented is clean for this test
        mock_input.side_effect = ["book1", "q"]
        
        lms.borrow_books()
        
        self.assertEqual(lms.books, {"book1": 1, "book2": 1})
        self.assertEqual(lms.books_rented, {"book1": 1, "book2": 0})
        # Check some key print calls
        # The initial availability listing print can be complex, focus on the borrow confirmation
        self.assertIn(call("You have borrowed 'book1', 1 copies remain."), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_borrow_unavailable_book(self, mock_input, mock_print, mock_sleep):
        lms.books = {"book1": 0, "book2": 1}
        lms.books_rented = {"book1": 0, "book2": 0}
        mock_input.side_effect = ["book1", "book2", "q"]
        
        lms.borrow_books()
        
        self.assertEqual(lms.books, {"book1": 0, "book2": 0})
        self.assertEqual(lms.books_rented, {"book1": 0, "book2": 1})
        self.assertIn(call("We're sorry, but that book isn't available."), mock_print.call_args_list)
        self.assertIn(call("You have borrowed 'book2', 0 copies remain."), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_borrow_non_existent_book(self, mock_input, mock_print, mock_sleep):
        lms.books = {"book1": 1}
        lms.books_rented = {"book1": 0}
        original_books_state = copy.deepcopy(lms.books)
        original_rented_state = copy.deepcopy(lms.books_rented)
        mock_input.side_effect = ["nonExistentBook", "q"]
        
        lms.borrow_books()
        
        self.assertEqual(lms.books, original_books_state)
        self.assertEqual(lms.books_rented, original_rented_state)
        self.assertIn(call("We're sorry, but that book isn't available."), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_borrow_quit_immediately(self, mock_input, mock_print, mock_sleep):
        lms.books = {"book1": 1}
        lms.books_rented = {"book1": 0}
        original_books_state = copy.deepcopy(lms.books)
        original_rented_state = copy.deepcopy(lms.books_rented)
        mock_input.side_effect = ["q"]
        
        lms.borrow_books()
        
        self.assertEqual(lms.books, original_books_state)
        self.assertEqual(lms.books_rented, original_rented_state)
        # Ensure no borrow messages were printed
        borrow_messages_found = any("You have borrowed" in str(c) for c in mock_print.call_args_list)
        self.assertFalse(borrow_messages_found)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_borrow_all_copies_of_a_book(self, mock_input, mock_print, mock_sleep):
        lms.books = {"book1": 1}
        lms.books_rented = {"book1": 0}
        mock_input.side_effect = ["book1", "q"]
        
        lms.borrow_books()
        
        self.assertEqual(lms.books, {"book1": 0})
        self.assertEqual(lms.books_rented, {"book1": 1})
        self.assertIn(call("You have borrowed 'book1', 0 copies remain."), mock_print.call_args_list)


    # 3. Tests for return_books()
    @patch('builtins.print')
    @patch('builtins.input')
    def test_return_borrowed_book(self, mock_input, mock_print, mock_sleep):
        lms.books = {"book1": 0}
        lms.books_rented = {"book1": 1} # book1 is rented
        mock_input.side_effect = ["book1", "q"]
        
        lms.return_books()
        
        self.assertEqual(lms.books, {"book1": 1})
        self.assertEqual(lms.books_rented, {"book1": 0})
        self.assertIn(call("You have returned a copy of book1. Now there is 0 copy not returned."), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_return_book_not_borrowed_or_non_existent(self, mock_input, mock_print, mock_sleep):
        lms.books = {"book1": 1, "book2": 0}
        lms.books_rented = {"book1": 0, "book2": 1} # book2 is rented, book1 is not
        original_books_state = copy.deepcopy(lms.books)
        original_rented_state = copy.deepcopy(lms.books_rented)
        
        # Attempt to return book1 (not rented out, though exists)
        mock_input.side_effect = ["book1", "q"]
        lms.return_books()
        self.assertIn(call("That book is not rented out."), mock_print.call_args_list)
        self.assertEqual(lms.books, original_books_state)
        self.assertEqual(lms.books_rented, original_rented_state)
        mock_print.reset_mock()

        # Attempt to return nonExistentBook
        mock_input.side_effect = ["nonExistentBook", "q"]
        lms.return_books()
        self.assertIn(call("That book is not rented out."), mock_print.call_args_list)
        self.assertEqual(lms.books, original_books_state)
        self.assertEqual(lms.books_rented, original_rented_state)


    @patch('builtins.input')
    def test_return_quit_immediately(self, mock_input, mock_sleep):
        lms.books = {"book1": 0}
        lms.books_rented = {"book1": 1}
        original_books_state = copy.deepcopy(lms.books)
        original_rented_state = copy.deepcopy(lms.books_rented)
        mock_input.side_effect = ["q"]
        
        lms.return_books()
        
        self.assertEqual(lms.books, original_books_state)
        self.assertEqual(lms.books_rented, original_rented_state)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_return_when_no_books_rented(self, mock_input, mock_print, mock_sleep):
        # Setup: No books are currently rented out that are part of the main 'books' dict
        lms.books = {"book1": 1, "book2": 2}
        lms.books_rented = {"book1": 0, "book2": 0} # No copies of book1 or book2 are rented
        
        # The function's `borrowed_books` list will be empty.
        # `books_not_returned` will become False.
        # The `while books_not_returned:` loop should not run.
        lms.return_books()
        
        # Assert that input was never called because the loop should not have been entered.
        mock_input.assert_not_called()
        # Assert that no print calls related to listing books to return were made.
        # (The function might print a message if no books are rented, this depends on its exact logic)
        # Based on current code, if borrowed_books is empty, it just skips the loop.
        # Let's check that no prompts for book names or "has x non-returned copies" were printed.
        for c_args, _ in mock_print.call_args_list:
            self.assertNotIn("has 0 non-returned copies", c_args[0]) # Example of a print within the loop
            self.assertNotIn("has 1 non-returned copies", c_args[0]) 
        # More robustly, we can count calls if there's a specific "no books to return" message outside the loop.
        # For now, assuming no specific message, so no calls to print from within the loop logic.
        # If there was a print *before* the loop, that would be fine.
        # The current code does not print anything if borrowed_books is empty.

if __name__ == '__main__':
    unittest.main()
