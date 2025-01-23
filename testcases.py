import unittest
import functions

class Lab3TestCases(unittest.TestCase):
    def test_double_one(self):
        result = functions.double(2)
        expected = 4
        self.assertEqual(expected, result)

    def test_double_two(self):
        result = functions.double(3)
        expected = 9
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
#Question: If test_double_one had been the only testing function,
# the tests would have passed the first time. Would that have meant that the code was
# correct? While waiting to demonstrate completion of the lab,
# ponder how many tests one might need to sufficiently test this function.
#Just because test_double_one would've been the only right one wouldn't mean the code is correct
#for all outcomes