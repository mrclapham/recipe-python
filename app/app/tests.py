"""
Sample test cases
"""

from django.test import SimpleTestCase

from app import calc


class CalcTestCases(SimpleTestCase):
    """Test the calc model"""
    def test_add(self):
        """Test the add function from the calc module."""
        res = calc.add(3, 8)
        
        self.assertEqual(res, 11)
        
    def test_subtract(self):
        """Test the subtract function from the calc module."""
        res = calc.subtract(5, 11)
        
        self.assertEqual(res, 6)        
