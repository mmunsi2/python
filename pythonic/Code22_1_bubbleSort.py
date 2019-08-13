def bubble(list):

	length = len(list) - 1
	sorted = False

	while not sorted:

		sorted = True

		for i in range(length):

			if list[i] > list[i + 1]:

				sorted = False

				list[i], list[i + 1] = list[i + 1], list[i]

	return list

print bubble([3, 6, 2, 5, 1, 6, 2])