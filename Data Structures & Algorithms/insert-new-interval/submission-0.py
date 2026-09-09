class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        
        start_new = newInterval[0]
        end_new = newInterval[1]
        
        while i < n and intervals[i][1] < start_new:
            res.append(intervals[i])
            i += 1
            
        while i < n and intervals[i][0] <= end_new:
            start_new = min(start_new, intervals[i][0])
            end_new = max(end_new, intervals[i][1])
            i += 1
        res.append([start_new, end_new])
        
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res
