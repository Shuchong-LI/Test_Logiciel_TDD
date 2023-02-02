
def verify_table_size(l):
	if len(l) != 9:
		return False

	for i in range(len(l)):
		if len(l[i]) != 9:
			return False
	return True

def verify_element(l):

	for i in range(len(l)):
		for j in range(len(l[i])):
			if not isinstance(l[i][j],int):
				return False

	for i in range(len(l)):
		for j in range(len(l[i])):
			if l[i][j] > 9 or l[i][j] < 1:
				return False

	return True

def verify_row(l):

	l_flag = [0,0,0,0,0,0,0,0,0]

	if not verify_table_size(l) or not verify_element(l):
		return False

	for i in range(len(l)):
		for j in range(len(l[i])):
			if l_flag[(l[i][j]-1)] == 0 :
				l_flag[(l[i][j]-1)] = 1
			else :
				return False
		
		if l_flag != [1,1,1,1,1,1,1,1,1]:
			return False
		
		l_flag = [0,0,0,0,0,0,0,0,0]

	return True

def verify_column(l):

	l_flag = [0,0,0,0,0,0,0,0,0]

	if not verify_table_size(l) or not verify_element(l):
		return False

	for i in range(len(l)):
		for j in range(len(l[i])):
			if l_flag[(l[j][i]-1)] == 0 :
				l_flag[(l[j][i]-1)] = 1
			else :
				return False

		if l_flag != [1,1,1,1,1,1,1,1,1]:
			return False

		l_flag = [0,0,0,0,0,0,0,0,0]

	return True

def verify_block(l):
	l_flag = [0,0,0,0,0,0,0,0,0]

	if not verify_table_size(l) or not verify_element(l):
		return False

	for i in range(0,len(l),3):
		for j in range(0,len(l[i]),3):
			l_flag[(l[j][i]    -1)] += 1
			l_flag[(l[j][i+1]  -1)] += 1
			l_flag[(l[j][i+2]  -1)] += 1
			l_flag[(l[j+1][i]  -1)] += 1
			l_flag[(l[j+1][i+1]-1)] += 1
			l_flag[(l[j+1][i+2]-1)] += 1
			l_flag[(l[j+2][i]  -1)] += 1
			l_flag[(l[j+2][i+1]-1)] += 1
			l_flag[(l[j+2][i+2]-1)] += 1
			if l_flag != [1,1,1,1,1,1,1,1,1]:
				return False

			l_flag = [0,0,0,0,0,0,0,0,0]

	return True