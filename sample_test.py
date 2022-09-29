import unittest


def sum(x, y):
    result = x + y
    return result

# Unittest test classes must inherit from the unittest.TestCase class.
class SampleTest(unittest.TestCase): 
    def setUp(self):
        print("\nRun setUp")

    def tearDown(self):
        print("Run tearDown")

    @unittest.expectedFailure
    def test_sum_pos_int(self):
        self.assertEqual(sum(4, 6), 0)
# The assertEqual() method is inherited from the unittest.TestCase class.	It works in a similar way as using the assert statement with an equality condition, as in: assert first_value == second_value


    def test_sum_neg_int(self):
        self.assertEqual(sum(-4, -6), -10)

    def test_sum_pos_float(self):
        self.assertEqual(sum(4.5, 6.2), 10.7)

    @unittest.skip('demonstrating skipping')
    def test_sum_neg_float(self):
        self.assertEqual(sum(-4.5, -6.2), -10.7)

if __name__ == '__main__':
    unittest.main()


