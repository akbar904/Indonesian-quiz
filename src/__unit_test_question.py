
import unittest
from question import Question

class TestQuestion(unittest.TestCase):
	def setUp(self):
		self.options = ["1945", "1946", "1947", "1948"]
		self.question = Question("In what year did Indonesia gain independence?", "1945", self.options)

	def test_get_question(self):
		self.assertEqual(self.question.get_question(), "In what year did Indonesia gain independence?")

	def test_get_correct_answer(self):
		self.assertEqual(self.question.get_correct_answer(), "1945")

	def test_get_options(self):
		self.assertEqual(self.question.get_options(), self.options)

if __name__ == '__main__':
	unittest.main()
