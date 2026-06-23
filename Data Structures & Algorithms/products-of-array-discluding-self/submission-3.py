class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Zero scenario
        idx = -1
        res = []
        if 0 in nums:
            k = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    k *= nums[i]
                else:
                    if idx != -1:
                        return [0] * len(nums)
                    else:
                        idx = i
            res = [0] * (len(nums)-1)
            res.insert(idx, k)
            return res
        k = 1
        for num in nums:
            if num == 0:
                continue
            k *= num
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(k)
                k = 0
            else:
                res.append(k // nums[i])
        return res