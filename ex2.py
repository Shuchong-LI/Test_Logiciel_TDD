
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