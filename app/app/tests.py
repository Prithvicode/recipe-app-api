"""
Sample tests
"""


from django.test import SimpleTestCase  #no db integration needed

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self): # start with test
        """Test adding numbers together"""
        res = calc.add(6,6)
        self.assertEqual(res,12)

    def test_sub_numbers(self):
        res = calc.subtract(10,15)
        self.assertEqual(res,5)