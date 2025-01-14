import unittest
from math_quiz.math_quiz import generate_random_integer, generate_random_operator, question_generator


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        result = generate_random_operator() 
        self.assertIn(result, ['+', '-', '*'], f"Operator {result} is not one of ['+', '-', '*']") 
        
    def test_question_generator(self):
        test_cases = [ 
             (5, 2, '+', '5 + 2', 7), 
             (5, 2, '-', '5 - 2', 3), 
             (5, 2, '*', '5 * 2', 10) 
             ]
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = question_generator(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Problem {problem} does not match expected {expected_problem}") 
            self.assertEqual(answer, expected_answer, f"Answer {answer} does not match expected {expected_answer}")

if __name__ == "__main__":
    unittest.main()
