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

def isSuiteArethmetique(l):
	# The input should be a list!
	if not isinstance(l,list):
		return False

	# All variables in the list should be numeric!
	for n in l:
		if not isinstance(n,(int,float)):
			return False

	# The sequence should contain at least 3 element!
	if len(l) < 3:
		return False

	# This sequence is not a arethmetic sequence！
	for n in range(len(l)-2):
		if l[n+2] + l[n] != l[n+1] + l[n+1]:
			return False

	return True

def G_n_suivant(n_suiv,l):
	# The first input should be an int!
	if not isinstance(n_suiv,int) :
		return False
	# The second input should be a iist!
	if not isSuiteGeometrique(l):
		return False

	l_suiv = list()

	for i in range(n_suiv):
		l_suiv.append((l[1]/l[0])**(i+1)*l[-1])


	return True,l_suiv
