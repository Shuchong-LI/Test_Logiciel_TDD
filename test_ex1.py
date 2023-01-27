import ex1
import unittest

class test_ex1(unittest.TestCase):
	def test_isSuiteGeometrique(self):
		print("testing isSuiteGeometrique...")

		#integer list
		self.assertEqual(ex1.isSuiteGeometrique([1,2,4,8,16]),True)
		self.assertEqual(ex1.isSuiteGeometrique([2,4,8,16,32]),True)
		self.assertEqual(ex1.isSuiteGeometrique([3,9,27,81]),True)
		self.assertEqual(ex1.isSuiteGeometrique([4,20,100,500]),True)

		#float list (some of them does not work because of the mul/div precision)
		self.assertEqual(ex1.isSuiteGeometrique([1.2,1.44,1.728,2.0736]),True)
		self.assertEqual(ex1.isSuiteGeometrique([2.5,6.25,15.625,39.0625]),True)

		#fault test
		self.assertEqual(ex1.isSuiteGeometrique("I am not a list"),False)
		self.assertEqual(ex1.isSuiteGeometrique([0,0,0,0,0]),False)
		self.assertEqual(ex1.isSuiteGeometrique([1,2,3,4,5]),False)
		self.assertEqual(ex1.isSuiteGeometrique([1,2,'a','b','c']),False)
		self.assertEqual(ex1.isSuiteGeometrique([2,4]),False)




