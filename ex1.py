import math

def isSuiteGeometrique(l):
	# The input should be a list!
	if not isinstance(l,list):
		return False

	# All variables in the list should be numeric!
	for n in l:
		if not isinstance(n,(int,float)):
			return False

	# The list should not contain zero
	if l.count(0) > 0 :
		return False

	# The sequence should contain at least 3 element!
	if len(l) < 3:
		return False

	# This sequence is not a geometric sequence！
	for n in range(len(l)-2):
		if l[n+2]*l[n] != l[n+1]**2:
			return False

	return True
