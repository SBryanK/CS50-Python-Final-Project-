# test_program.py

import unittest
from unittest.mock import patch, Mock
from io import StringIO
import sys

# Import the functions from the main code
# Ensure the main code is saved as 'main_code.py' in the same directory
from main_code import (
    fetch_all_water_supply_data,
    fetch_water_supply_data,
    display_water_supply_data,
    display_top_10_water_supply_countries,
)

class TestWaterSupplyData(unittest.TestCase):
    @patch('main_code.requests.get')
    def test_fetch_all_water_supply_data(self, mock_get):
        # Mock API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {'name': {'common': 'CountryA'}, 'population': 1000000},
            {'name': {'common': 'CountryB'}, 'population': 2000000},
        ]
        mock_get.return_value = mock_response

        data = fetch_all_water_supply_data()
        self.assertIsNotNone(data)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name']['common'], 'CountryA')
        self.assertEqual(data[1]['population'], 2000000)

    @patch('main_code.requests.get')
    def test_fetch_water_supply_data(self, mock_get):
        # Mock API response for a specific country
        country_name = 'Singapore'
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                'name': {'common': country_name},
                'population': 5700000,
                'area': 728.6,
                'naturalResources': ['Fish', 'Deepwater ports'],
                'region': 'Asia',
            }
        ]
        mock_get.return_value = mock_response

        data = fetch_water_supply_data(country_name)
        self.assertIsNotNone(data)
        self.assertEqual(data['name']['common'], country_name)
        self.assertEqual(data['population'], 5700000)

    @patch('main_code.fetch_water_supply_data')
    def test_display_water_supply_data(self, mock_fetch):
        # Mock the fetch_water_supply_data function
        country_name = 'Singapore'
        mock_fetch.return_value = {
            'name': {'common': country_name},
            'population': 5700000,
            'area': 728.6,
            'naturalResources': ['Fish', 'Deepwater ports'],
            'region': 'Asia',
        }

        # Capture the console output
        captured_output = StringIO()
        sys.stdout = captured_output

        display_water_supply_data(country_name)

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn(f"Water Supply Data for {country_name}", output)
        self.assertIn("Population Density", output)
        self.assertIn("Natural Resources", output)

    @patch('main_code.fetch_all_water_supply_data')
    def test_display_top_10_water_supply_countries(self, mock_fetch_all):
        # Mock the fetch_all_water_supply_data function
        mock_fetch_all.return_value = [
            {'name': {'common': f'Country{i}'}, 'population': i * 1000000}
            for i in range(1, 12)
        ]

        # Capture the console output
        captured_output = StringIO()
        sys.stdout = captured_output

        display_top_10_water_supply_countries()

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Top 10 Countries by Population", output)
        self.assertIn("Country11", output)
        self.assertNotIn("Country1", output)  # Should not be in top 10

if __name__ == '__main__':
    unittest.main()
