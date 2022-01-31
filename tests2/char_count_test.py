import unittest
from keyFunctions import KeyFunctions

class FunctionsTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.func = KeyFunctions()

	def test_counting_chars(self):
		""" 
		Tests taking a string and returning a count of symbols, digits, and chars
		"""
		self.assertEqual(self.func.countChars('P@#yn26at^&i5ve'), {'chars': 8, 'symbols': 4, 'digits': 3})

if __name__ == '__main__':
    unittest.main()
