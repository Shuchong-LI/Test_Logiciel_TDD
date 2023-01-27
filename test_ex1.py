import ex1
import unittest

class test_ex1(unittest.TestCase):
	def test_function_ex1(self):
		print("testing function_ex1...")
		self.assertEqual(ex1.function_ex1(),"hello ex1!")
		self.assertNotEqual(ex1.function_ex1(),"Bye ex1!")		