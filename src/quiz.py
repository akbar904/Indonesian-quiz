
class Quiz:
	def __init__(self, questions):
		self.questions = questions

	def get_question(self, index):
		return self.questions[index]

	def get_total_questions(self):
		return len(self.questions)
