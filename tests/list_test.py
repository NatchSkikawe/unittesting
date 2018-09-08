import unittest
from list import count_unique, binary_search


class TestList(unittest.TestCase):

    def borderline_cases(self):
        self.assertEquals(count_unique([]),0)

    def typical_cases(self):
        l=["A","a","a","A","c","c","B"]
        self.assertEquals(count_unique(list),4)

    def impossible_cases(self):
        l =[2,"3"]
        with self.assertRaises(TypeError):self.count_unique[:1]

    def extreme_cases(self):
        l = ["a","a","a","a","a","a","a","a","a","a","a","a"]
        self.assertEquals(count_unique(list), 12 )

class TestBinarySearch(unittest.TestCase):

    def empty_case(self):
         list = []
         self.assertEqual("The list is empty", binary_search(list, 5))

    def target_is_none(self):
        list = [1, 2, 3, 4]
        self.assertEqual("None", binary_search(list, 5))

    def element_is_none(self):
        list = [1, 2, 3, 4, 5, 6, 7]
        binary_search(list, None)
        self.assertRaises(TypeError)

    def extreme_cases(self):
        list = []
        for i in range(1, 55555):
         list.append(i)
        self.assertEqual(55555, binary_search(list, 666666))

if __name__ == "__main__":
    unittest.main()