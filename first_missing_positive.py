class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mins = 0
        for l in nums:
            if l>0:
                mins =l
                break
        if mins == 0:
            return 1
        for k in nums:
            if k>0 and k<mins:
                mins = k
        if mins>1 :
            return 1
        else:
            while (mins in nums):
                mins += 1
            return mins
