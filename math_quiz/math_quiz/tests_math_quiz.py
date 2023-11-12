import unittest
from math_quiz import generate_random_integer, generate_random_operator, perform_operation

class MathGame_Test(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_value = 1
        max_value = 10
        for _ in range(1000):  # To test a large number of random values
            rand_num = generate_random_integer(min_value, max_value)
            self.assertTrue(min_value <= rand_num <= max_value)

    def test_generate_random_operator(self):
        # Test if the generated operator is one of '+', '-', or '*'
        Operators = set(['+', '-', '*'])
        for _ in range(1000):  # To test a large number of random values
            random_operator = generate_random_operator()
            self.assertIn(random_operator, Operators)

    def test_perform_operation(self):
        # Testing if the operation has happened successfully.
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = perform_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
