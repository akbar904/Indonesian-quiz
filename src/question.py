
class Question:
	def __init__(self, question: str, correct_answer: str, options: list):
		self._question = question
		self._correct_answer = correct_answer
		self._options = options

	def get_question(self):
		return self._question

	def get_correct_answer(self):
		return self._correct_answer

	def get_options(self):
		return self._options
