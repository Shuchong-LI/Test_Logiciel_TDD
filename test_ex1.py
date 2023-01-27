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

	def test_isSuiteArethmetique(self):
		print("testing isSuiteArethmetique...")

		#integer list
		self.assertEqual(ex1.isSuiteArethmetique([0,0,0,0,0]),True)
		self.assertEqual(ex1.isSuiteArethmetique([1,2,3,4,5]),True)
		self.assertEqual(ex1.isSuiteArethmetique([2,4,6,8,10]),True)
		self.assertEqual(ex1.isSuiteArethmetique([3,9,15,21]),True)
		self.assertEqual(ex1.isSuiteArethmetique([4,20,36,52]),True)

		#float list 
		self.assertEqual(ex1.isSuiteArethmetique([1.2,2.4,3.6,4.8]),True)
		self.assertEqual(ex1.isSuiteArethmetique([2.5,5,7.5.10,12.5]),True)

		#fault test
		self.assertEqual(ex1.isSuiteArethmetique("I am not a list"),False)
		self.assertEqual(ex1.isSuiteArethmetique([1,2,3,4,7]),False)
		self.assertEqual(ex1.isSuiteArethmetique([1,2,'a','b','c']),False)





