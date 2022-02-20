class Solution:    
    def fractionalknapsack(self, W,items,n):
        if W == 0:
            return 0
        l = []
        for i in items:
            l.append([i.value, i.weight])
        l.sort(key = lambda x: -x[0]/x[1])
        total = 0
        for i in l:
            if W == 0:
                return total
            if i[1] > W:
                total += (i[0]/(i[1]/W))
                W = 0
            elif i[1] <= W:
                total += i[0]
                W -= i[1]
        return (total)
