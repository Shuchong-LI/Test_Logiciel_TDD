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



class test_ex2(unittest.TestCase):
	#table 9x9
	def test_verify_table_size(self):
		print("testing verify_table_size...")

		self.assertTrue(ex2.verify_table_size(l1))
		self.assertFalse(ex2.verify_table_size(l2))
		self.assertFalse(ex2.verify_table_size(l3))
	#num 1-9
	# def test_verify_int_range(self):

		
	# def test_verify_row(self):

	# def test_verify_column(self):

	# def test_verify_block(self):

	# def test_verify_sudoku(self):
	# 	print("testing verify_sudoku...")




