
def verify_table_size(l):
	if len(l) != 9:
		return False

	for i in range(len(l)):
		if len(l[i]) != 9:
			return False
	return True