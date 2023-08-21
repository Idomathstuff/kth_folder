def heapify(arr, N, i):

	largest = i  
	l = 2 * i + 1  
	r = 2 * i + 2  

	if l < N and arr[l] > arr[largest]:
		largest = l # left becomes largest

	if r < N and arr[r] > arr[largest]:
		largest = r # right becomes largest

	if largest != i: # if the chosen index isn't largest
		arr[i], arr[largest] = arr[largest], arr[i] # switch the index of the largest and the index of the chosen index
		heapify(arr, N, largest) # won't do anything if the new data point that was switched is already heapified

def buildHeap(arr, N):
	startIdx = N // 2 - 1 
	for i in range(startIdx, -1, -1): #starts at the middle at the last non leaf node and goes down towards the first element
		heapify(arr, N, i)

def printHeap(arr, N):
	print("Array representation of Heap is:")

	for i in range(N):
		print(arr[i], end=" ")
	print()


if __name__ == '__main__':
    # a = range(10,1,-1) # reverses starting from 10 up to 1 in steps of 2
    pass
    arr = [1, 3, 5, 4, 6, 13,10, 9, 8, 15, 17]
    N = len(arr)
    buildHeap(arr, N)
    printHeap(arr, N)

