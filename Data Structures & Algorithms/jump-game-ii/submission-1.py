class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        
        # Memoization table to store: { index: min_jumps_from_here }
        memo = {}
        
        def get_min_jumps(i):
            if i >= goal:
                return 0
            if i in memo:
                return memo[i]
                
            min_distance = float("inf")
            
            for jump in range(1, nums[i] + 1):
                next_index = i + jump
                jumps_from_next = get_min_jumps(next_index)
                if jumps_from_next != float("inf"):
                    min_distance = min(min_distance, 1 + jumps_from_next)
            
            memo[i] = min_distance
            return min_distance
            
        return get_min_jumps(0)
