arr = ["apples", "oranges", "bananas", "grapes"]
s = "cherries"
found = False
size = len(arr)
for i in range(0, size):
    if arr[i] == s:
        found = True
print(found)
#from https://towardsdatascience.com/how-to-be-pythonic-and-why-you-should-care-188d63a5037e