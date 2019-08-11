# Python program for implementation of heap Sort 
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(array, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and array[i] < array[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and array[largest] < array[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        array[i],array[largest] = array[largest],array[i]  # swap 
  
        # Heapify the root. 
        heapify(array, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(array): 
    n = len(array) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(array, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        array[i], array[0] = array[0], array[i]   # swap 
        heapify(array, i, 0) 
  
# Driver code to test above 
array = [ 12, 11, 13, 5, 6, 7] 
heapSort(array) 
n = len(array) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %array[i]), 
# This code is contributed by Mohit Kumra 
