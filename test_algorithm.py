import unittest
from algorithm import append_and_sort

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.array = [3,2]

    def test_successful(self):
        self.assertEqual(append_and_sort(self.array,1,5),[1,2,3,5])

if __name__ == '__main__':
    unittest.main()
