class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # min_height(value) * width(index_diff) = area
        # Input: height = [1,7,2,5,4,7,3,6]
        # i = 0, j = 7 -> min_height = 1, width = 7 -> area = 7
        # num[i] < num[j] -> i = 1, j = 7 -> min_height = 6, width = 6 -> area = 36
        max_area = -1
        i = 0
        j = len(heights) - 1
        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            if area > max_area:
                max_area = area
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area 