import unittest
from algorithm import append_and_sort

class TestSearch(unittest.TestCase):
	def setUp(self):
		self.array = [3,2]

	def test_successful(self):
		self.assertEqual(append_and_sort(self.array,1,5),[1,2,3,5])
	
	
	def test_whenArrayIsNone(self):
		self.assertFalse(None, 10)
	
	def test_empty_same_parameters(self):
		self.assertTrue(append_and_sort(self.array,0,0),[0,2,3])

	
	def test_emptyArray(self):
		self.assertFalse(append_and_sort([], None,None))

	def test_emptyToFull(self):
		self.assertEqual(append_and_sort([],5,10), [5,10])
	
	
if __name__ == '__main__':
	unittest.main()
