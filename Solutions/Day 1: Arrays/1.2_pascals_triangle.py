class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list = []
        for i in range(numRows):
            list.append([])
            for j in range(i+1):
                if j==0 or j==i:
                    list[i].append(1)
                else:
                    list[i].append(list[i-1][j-1]+list[i-1][j])
        return list
