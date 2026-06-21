class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_list = sorted(nums)
        for idx, num in enumerate(sorted_list):
            if idx+1 == len(sorted_list):
                return False
            if num == sorted_list[idx+1]:
                return True
        return False