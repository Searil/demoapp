def append_and_sort(array, number1, number2):
	# check if parameters stored in array
	# if not append and sort

    if number1 not in array:
        array.append(number1)
    if number2 not in array:
        array.append(number2)

    return sorted(array)
