#1.Excercise Create a function that takes a list of numbers as parameter and returns the average value of the odd numbers in the list.
def list_odd(my_list):
	my_list_odd=[]
	for i in range(len(my_list)):
		if my_list[i] % 2 != 0:
			my_list_odd.append(my_list[i])
	if len(my_list_odd) == 0:
		print ('The list is empty')
	else:
		mean=sum(my_list_odd)/len(my_list_odd)
		print float(mean)