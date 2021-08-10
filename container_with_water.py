class Solution:
    def maxArea(self, height: List[int]) -> int:
        lft = 0
        rgt = len(height) - 1
        mx = 0
        cnt = 0
        while lft <= rgt:
            if height[lft] <= height[rgt]:
                cnt = height[lft]*(rgt-lft)
                lft += 1
            else:
                cnt = height[rgt]*(rgt-lft)
                rgt -= 1
            mx = cnt if cnt > mx else mx
