def getInversions(arr, n):
	ctr = 0
	for i in range(n-1):
		for j in range(i+1, n):
			if arr[i] > arr[j] and i < j:
				ctr += 1
	return ctr
