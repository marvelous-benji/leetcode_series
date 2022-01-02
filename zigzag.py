import time


def zigzag(s, n):
    m = len(s)
    if m <= n or n == 1:
        return s
    k = 0
    res = ''
    st = 2 * (n - 1)
    ed = 0
    while k < n:
        p = k
        res += s[p]
        while p + st < m:
            if ed == 0:
                res += s[p + st]
                p += st
            elif st == 0:
                if p + ed < m:
                    res += s[p+ed]
                    p += ed
                else:
                    break
            else:
                res += s[p + st]
                p += st
                if p + ed < m:
                    res += s[p+ed]
                    p += ed
                else:
                    break
        st -= 2
        ed += 2
        k += 1
    return res

s = 'ABCDEFGHI'
n = 2
st = time.time()
print(zigzag(s,n))
print(time.time() - st)



