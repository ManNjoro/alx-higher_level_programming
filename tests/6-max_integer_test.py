#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reversed_list(self):
        """Test with a reversed list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_duplicate_numbers(self):
        """Test with a list containing duplicate numbers"""
        self.assertEqual(max_integer([1, 2, 3, 2, 1]), 3)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)
    
    def test_mixed_numbers(self):
        result = max_integer([-10, 5, -3, 0, 7, -2])
        self.assertEqual(result, 7)
    
    def test_large_list(self):
        lst = list(range(1, 10001))
        result = max_integer(lst)
        self.assertEqual(result, 10000)
    
    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)
    
    def test_max_integer_with_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")
        self.assertEqual(max_integer(["cat", "dog", "elephant"]), "elephant")
        self.assertEqual(max_integer(["Hello", "World"]), "World")
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertEqual(max_integer(["abc", "def", "ghi"]), "ghi")
    

    def test_max_integer_with_non_list_input(self):
        with self.assertRaises(TypeError):
            max_integer(123)
        with self.assertRaises(TypeError):
            max_integer("hello")
        with self.assertRaises(TypeError):
            max_integer(("a", "b", "c"))

if __name__ == '__main__':
    unittest.main()