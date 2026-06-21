class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        newList = []
        for idx, num in enumerate(nums):
            if dict.get(target - num, -1) >= 0 and idx != dict[target-num]:
                newList.append(min(idx, dict[target-num]))
                newList.append(max(idx, dict[target-num]))
                return newList
            dict[num] = idx
            