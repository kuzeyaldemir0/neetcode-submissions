class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # num1 + num2 + num3 = 0 is eq. to num1 + num2 = -1 * num3
        # nums = [-1,0,1,2,-1,-4]
        # sorted = [-4, -1, -1, 0, 1, 2]
        # target is -1 since it's in the middle so -1 * -1 = 1 is real target
        # We'll check for each pair from both start and end to see whether we can capture
        # the real target. 
        res = []
        nums.sort()
        for idx, num in enumerate(nums):
            if num > 0: break
            if idx != 0 and num == nums[idx-1]:
                continue
            target = -1 * num
            i = idx + 1
            j = len(nums) - 1
            while i < j:                
                if nums[i] + nums[j] == target:
                    res.append([num, nums[i], nums[j]])
                    i += 1 
                    j -= 1

                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        return res