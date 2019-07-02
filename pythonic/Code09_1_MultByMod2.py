x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for idx in range(len(x)):
	if x[idx]%2==0:
		result.append(x[idx] * 2)
else:
	result.append(x[idx])
#print(result)