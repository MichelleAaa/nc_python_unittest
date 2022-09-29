import unittest

def sum(x, y):
    result = x + y
    return result

# Unittest test classes must inherit from the unittest.TestCase class.

class SampleTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(4, 6), 0)
        self.assertEqual(sum(-4, -6), -10)
        self.assertEqual(sum(4.5, 6.2), 10.7)
        self.assertEqual(sum(-4.5, -6.2), -10.7)


if __name__ == '__main__':
    unittest.main()
