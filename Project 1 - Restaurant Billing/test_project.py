import unittest
from unittest.mock import patch
import io
import sys
import os
import csv
from prettytable import PrettyTable

# Import the functions and data from the main code
# Make sure the original code is saved as 'main_code.py' or adjust the import accordingly
from main_code import menu, order, display, take_o, save_order, review_order, calculate_bill

class TestOrderingSystem(unittest.TestCase):
    def setUp(self):
        # Reset the order before each test
        self.order = []

    def test_display(self):
        # Capture the output of display()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        display()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        # Now check if output contains the menu items and prices
        for index, (item, price) in enumerate(menu.items(), 1):
            expected_line = f"{index}. {item}: ${price:.2f}"
            self.assertIn(expected_line, output)

    @patch('builtins.input', side_effect=['1', '2', 'e'])
    def test_take_o(self, mock_input):
        take_o(menu, self.order)
        expected_order = [('Hainanese Chicken Rice', 2)]
        self.assertEqual(self.order, expected_order)

    def test_save_order(self):
        # Prepare an order
        test_order = [('Hainanese Chicken Rice', 2), ('Satay', 1)]
        # Save the order
        save_order(test_order)
        # Now read 'Orders.csv' and check contents
        with open('Orders.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            expected_rows = [
                ['Item', 'Quantity'],
                ['Hainanese Chicken Rice', '2'],
                ['Satay', '1']
            ]
            self.assertEqual(rows, expected_rows)
        # Clean up
        os.remove('Orders.csv')

    def test_calculate_bill(self):
        test_order = [('Hainanese Chicken Rice', 2), ('Satay', 1)]
        total = calculate_bill(menu, test_order)
        expected_total = menu['Hainanese Chicken Rice'] * 2 + menu['Satay'] * 1
        self.assertEqual(total, expected_total)

    @patch('builtins.input', side_effect=['10', '1', 'e'])
    def test_take_o_invalid_input(self, mock_input):
        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        take_o(menu, self.order)
        sys.stdout = sys.__stdout__
        # Check that the error message is printed
        output = captured_output.getvalue()
        self.assertIn("Not Found, Please Try Again.", output)
        # Check that valid input was processed
        expected_order = [('Nasi Lemak', 1)]
        self.assertEqual(self.order, expected_order)

    def test_review_order(self):
        # Write a temporary 'Orders.csv' file
        test_order = [('Hainanese Chicken Rice', '2'), ('Satay', '1')]
        with open('Orders.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item', 'Quantity'])
            writer.writerows(test_order)
        # Capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        review_order()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        # Check that the output contains the expected table
        self.assertIn("Your Final Order:", output)
        self.assertIn("Hainanese Chicken Rice", output)
        self.assertIn("Satay", output)
        # Clean up
        os.remove('Orders.csv')

if __name__ == '__main__':
    unittest.main()
