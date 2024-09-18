
import unittest
from quiz import Quiz
from question import Question

class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.question1 = Question("When did Indonesia gain independence?", "1945", ["1945", "1946", "1947", "1948"])
        self.question2 = Question("Who is the first president of Indonesia?", "Soekarno", ["Soekarno", "Soeharto", "Jokowi", "SBY"])
        self.quiz = Quiz([self.question1, self.question2])
        
    def test_init(self):
        self.assertEqual(self.quiz.questions[0], self.question1)
        self.assertEqual(self.quiz.questions[1], self.question2)

    def test_get_question(self):
        self.assertEqual(self.quiz.get_question(0), self.question1)
        self.assertEqual(self.quiz.get_question(1), self.question2)
        
    def test_get_total_questions(self):
        self.assertEqual(self.quiz.get_total_questions(), 2)

if __name__ == '__main__':
    unittest.main()
