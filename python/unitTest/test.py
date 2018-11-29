import unittest
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_sum_tuple(self):
        """
        Test that it can sum a tuple of integers
        """
        data = (1, 2, 3)
        result = sum(data)
        self.assertEqual(result, 6)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)


if __name__ == '__main__':
    unittest.main()
