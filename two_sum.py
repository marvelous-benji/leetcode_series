class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finder = {}
        for i,k in enumerate(nums):
            x = target - k
            if finder.get(x,None) is not None:
                return [finder[x], i]
            else:
