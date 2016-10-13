def append_and_sort(array, number1, number2):
	# check if parameters stored in array
	# if not append and sort


    if number1 not in array and number1 is not None:
        array.append(number1)
    if number2 not in array and number2 is not None:
        array.append(number2)
    if len(array) == 0:
    	return False
    else:
    	return sorted(array)
