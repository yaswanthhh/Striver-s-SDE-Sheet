def findMinimumCoins(amount):
	denominations.sort(reverse = True)
	ctr = 0
	n = len(denominations)
	for i in denominations:
		if n >= i:
			ctr = ctr + n//i
			n = n % i
			if n == 0:
				return ctr
