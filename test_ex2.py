import ex2
import unittest

class test_ex2(unittest.TestCase):
	def test_function_ex2(self):
		print("testing function_ex2...")
		self.assertEqual(ex2.function_ex2(),"hello ex2!")
		self.assertNotEqual(ex2.function_ex2(),"Bye ex2!")		