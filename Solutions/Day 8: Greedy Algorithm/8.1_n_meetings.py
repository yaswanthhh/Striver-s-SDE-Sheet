class Solution:
    
    class MeetPair:
	    def __init__(self, start, end, pos):
		    self.start = start
		    self.end = end
		    self.pos = pos
		    
    def maximumMeetings(self,n,start,end):
        pairs = []
        for i in range(n):
            pairs.append(self.MeetPair(start[i], end[i], i))
        res, ctr = [], 1
        pairs.sort(key = lambda x: x.end)
        res.append(pairs[0].pos)
        prev = pairs[0].end
        for i in range(1, n):
            if pairs[i].start > prev:
                res.append(pairs[i].pos)
                prev = pairs[i].end
                ctr += 1
        return ctr
