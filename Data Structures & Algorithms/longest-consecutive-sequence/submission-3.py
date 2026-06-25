class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)
        best_count = 0
        for num in nums:
            if num-1 not in set_nums:
                count = 1
                while num+1 in set_nums:
                    num += 1
                    count += 1
                if count >= best_count:
                    best_count = count
        return best_count