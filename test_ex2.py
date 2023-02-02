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

# Good for rows
l8 = 	[[1,2,3,4,5,6,7,8,9],
		[2,1,3,4,5,6,7,8,9],
		[1,2,5,4,3,6,7,8,9],
		[6,2,3,4,5,1,7,8,9],
		[3,2,1,4,5,9,7,8,6],
		[2,1,3,4,6,5,7,8,9],
		[1,2,3,4,5,6,7,8,9],
		[1,2,3,4,5,6,7,8,9],
		[1,2,3,4,5,6,7,8,9]]

# Good for columns
l9 = 	[[1,9,3,5,1,4,1,2,8],
		[2,8,2,4,2,3,6,4,6],
		[3,7,1,3,9,2,7,6,4],
		[4,6,4,2,8,1,8,8,2],
		[5,5,5,1,7,5,9,1,9],
		[6,4,6,6,6,6,5,3,7],
		[7,3,9,7,5,7,4,9,5],
		[8,2,8,8,4,9,3,7,3],
		[9,1,7,9,3,8,2,5,1]]

#  good sudokgu
l10 = 	[[1,9,8,5,2,6,3,4,7],
		[7,2,5,3,4,1,6,9,8],
		[3,4,6,9,7,8,2,1,5],
		[9,8,1,2,5,7,4,6,3],
		[5,6,4,1,3,9,8,7,2],
		[2,3,7,6,8,4,1,5,9],
		[4,7,3,8,1,5,9,2,6],
		[8,1,9,7,6,2,5,3,4],
		[6,5,2,4,9,3,7,8,1]]



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


		
	def test_verify_row(self):
		print("testing verify_row...")

		self.assertFalse(ex2.verify_row(l1))
		self.assertFalse(ex2.verify_row(l2))
		self.assertFalse(ex2.verify_row(l3))

		self.assertFalse(ex2.verify_row(l4))
		self.assertFalse(ex2.verify_row(l5))
		self.assertFalse(ex2.verify_row(l6))
		self.assertFalse(ex2.verify_row(l7))

		self.assertTrue(ex2.verify_row(l8))
		self.assertFalse(ex2.verify_row(l9))
		self.assertTrue(ex2.verify_row(l10))

	def test_verify_column(self):
		print("testing verify_column...")

		self.assertFalse(ex2.verify_column(l1))
		self.assertFalse(ex2.verify_column(l2))
		self.assertFalse(ex2.verify_column(l3))

		self.assertFalse(ex2.verify_column(l4))
		self.assertFalse(ex2.verify_column(l5))
		self.assertFalse(ex2.verify_column(l6))
		self.assertFalse(ex2.verify_column(l7))

		self.assertFalse(ex2.verify_column(l8))
		self.assertTrue(ex2.verify_column(l9))
		self.assertTrue(ex2.verify_column(l10))

	# def test_verify_block(self):

	# def test_verify_sudoku(self):
	# 	print("testing verify_sudoku...")




