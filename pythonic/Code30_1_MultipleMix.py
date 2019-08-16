x=[1, 2, 3, 4, 5, 6]
result = []
for idx in range(len(x)):
	print(x[idx] * 2)



x=[1, 2, 3, 4, 5, 6]
[print(element * 2) for element in x]

#-----------

x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for idx in range(len(x)):
    if x[idx]%2==0:
        print(x[idx] * 2)





x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[print(element * 2) for element in x if element % 2 == 0]
