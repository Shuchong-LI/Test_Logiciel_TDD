import ex2
import unittest

# 9x9
l1 = 	[[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0]]

# 8x9
l2 = 	[[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0]]

# 9x8
l3 = 	[[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]

# 9x9 with elements not a number
l4 = 	[[1,1,1,1,"Hey,I am not an number",1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1]]

# 9x9 with float in it
l5 = 	[[1,1,1,1,2.34,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1]]

# 9x9 with int out of range
l6 = 	[[1,1,1,1,10,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1]]

# 9x9 and all the elements are in range [1,9]
l7 = 	[[1,2,1,1,1,1,1,1,9],
		[1,1,3,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,8,1],
		[1,4,1,1,1,7,1,1,1],
		[1,1,1,5,1,1,1,1,1],
		[1,1,1,1,6,1,1,1,1],
		[1,4,1,1,1,7,1,1,1],
		[5,1,1,3,1,1,8,1,1],
		[1,6,1,1,2,1,1,9,1]]



class test_ex2(unittest.TestCase):
	#table 9x9
	def test_verify_table_size(self):
		print("testing verify_table_size...")

		self.assertTrue(ex2.verify_table_size(l1))
		self.assertFalse(ex2.verify_table_size(l2))
		self.assertFalse(ex2.verify_table_size(l3))
	#num 1-9
	def test_verify_element(self):
		print("testing verify_element...")

		self.assertFalse(ex2.verify_element(l1))
		self.assertFalse(ex2.verify_element(l2))
		self.assertFalse(ex2.verify_element(l3))

		self.assertFalse(ex2.verify_element(l4))
		self.assertFalse(ex2.verify_element(l5))
		self.assertFalse(ex2.verify_element(l6))
		self.assertTrue(ex2.verify_element(l7))


		
	# def test_verify_row(self):

	# def test_verify_column(self):

	# def test_verify_block(self):

	# def test_verify_sudoku(self):
	# 	print("testing verify_sudoku...")




