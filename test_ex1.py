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
		self.assertEqual(ex1.isSuiteArethmetique([2.5,5,7.5,10,12.5]),True)
		# self.assertEqual(ex1.isSuiteArethmetique([1.1,2.2,3.3,4.4]),True) # precision fault

		#fault test
		self.assertEqual(ex1.isSuiteArethmetique("I am not a list"),False)
		self.assertEqual(ex1.isSuiteArethmetique([1,2,3,4,7]),False)
		self.assertEqual(ex1.isSuiteArethmetique([1,2,'a','b','c']),False)
		self.assertEqual(ex1.isSuiteArethmetique([1,2]),False)

	def test_G_n_suivant(self):
		print("testing G_n_suivant...")

		#integer list
		self.assertEqual(ex1.G_n_suivant(3,[1,2,4,8,16]),(True,[32,64,128]))
		self.assertEqual(ex1.G_n_suivant(2,[2,4,8,16,32]),(True,[64,128]))
		self.assertEqual(ex1.G_n_suivant(1,[3,9,27,81]),(True,[243]))
		self.assertEqual(ex1.G_n_suivant(4,[4,20,100,500]),(True,[2500,12500,62500,312500]))


		#fault test
		self.assertEqual(ex1.G_n_suivant(2,"I am not a list"),False)
		self.assertEqual(ex1.G_n_suivant("I am not an int",[1,2,4]),False)
		self.assertEqual(ex1.G_n_suivant("I am not an int","I am not a list"),False)
		self.assertEqual(ex1.G_n_suivant(3,[1,2,4,8,17]),False)




	def test_A_n_suivant(self):
		print("testing A_n_suivant...")

		#integer list
		self.assertEqual(ex1.A_n_suivant(3,[0,0,0,0,0]),(True,[0,0,0]))
		self.assertEqual(ex1.A_n_suivant(3,[1,2,3,4,5]),(True,[6,7,8]))
		self.assertEqual(ex1.A_n_suivant(2,[2,4,6,8,10]),(True,[12,14]))
		self.assertEqual(ex1.A_n_suivant(4,[3,9,15,21]),(True,[27,33,39,45]))
		self.assertEqual(ex1.A_n_suivant(1,[4,20,36,52]),(True,[68]))


		#fault test
		self.assertEqual(ex1.A_n_suivant(2,"I am not a list"),False)
		self.assertEqual(ex1.A_n_suivant("I am not an int",[1,2,4]),False)
		self.assertEqual(ex1.A_n_suivant("I am not an int","I am not a list"),False)
		self.assertEqual(ex1.A_n_suivant(3,[1,2,3,4,6]),False)






