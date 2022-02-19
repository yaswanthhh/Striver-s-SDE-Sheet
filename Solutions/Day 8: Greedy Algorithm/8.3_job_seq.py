class Solution:
    def JobScheduling(self,Jobs,n):
        profit = 0
        slot = [-1] * n
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        for job in Jobs:
            for j in reversed(range(job.deadline)):
                if j < n and slot[j] == -1:
                    slot[j] = job.id
                    profit += job.profit
                    break
        return[len(list(filter(lambda x: x != -1, slot))), profit]
