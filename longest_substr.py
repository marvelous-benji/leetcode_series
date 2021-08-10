class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = 0
        seen = {}
        cnt = 0
        mx = 0
        m = len(s)
        for k in range(m):
            if seen.get(s[k],'None') != 'None':
                if seen[s[k]] >= st:
                    st = seen[s[k]] + 1
                    seen[s[k]] = k
                    cnt = k - st + 1
                else:
                    cnt += 1
                    seen[s[k]] = k
            else:
                seen[s[k]] = k
                cnt += 1
            mx = cnt if cnt > mx else mx
