#!/usr/bin/python

def safe_print_list(my_list=[], x=0):
	""" A function that prints x elements of a list
	
	Args:
		my_list (list): the list
		x (int): the number of elements to print from the list
		
	Returns:
		The number of elements printed from the list
	"""
	r = 0
	for i in range(x):
		try:
			print("{}".format(my_list[i]), end="")
			r += 1
		except IndexError:
			break
	print("")
	return (r)
