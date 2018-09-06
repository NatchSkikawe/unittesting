import unittest
from list import count_unique


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
if __name__ == '__main__':
    unittest.main()