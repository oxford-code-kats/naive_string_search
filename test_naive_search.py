import unittest
from naive_search import word_search

class TestSearch(unittest.TestCase):

	def test_single_word_match(self):
		text = "hello world"
		search_term = "hello"
		counts = word_search(search_term, text)
		self.assertEqual(1, counts)

	def test_double_word_match(self):
		text = "hello hello"
		search_term = "hello"
		counts = word_search(search_term, text)
		self.assertEqual(2, counts)

	def test_complex_sentence(self):
		text = """here is a slightly harder sentence that 
		repeats the word here three times in total here."""
		search_term = "here"
		counts = word_search(search_term, text)
		self.assertEqual(3, counts)

if __name__ == "__main__":
	unittest.main()