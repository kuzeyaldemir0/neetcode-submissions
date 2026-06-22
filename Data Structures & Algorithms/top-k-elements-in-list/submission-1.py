class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)
        
        for num in nums:
            dict[num] += 1

        result = []
        for _ in range(k):
            curr_max_number = max(dict, key=dict.get)
            result.append(curr_max_number)
            del dict[curr_max_number]

        return result
        