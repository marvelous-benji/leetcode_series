
from random import shuffle


def check(arr, S):
    p = len(arr[0])
    m = p * len(arr)
    n = len(S)
    ar = []
    k = 0
    s = {}
    for i in arr:
        if s.get(i, None) is not None:
            s[i] += 1
        else:
            s[i] = 1
    while k <= n - m:
        dec = False
        if S[k:k+p] not in arr:
            k += 1
            continue
        else:
            r = [S[l:l+p] for l in range(k, m+k, p)]
            res = s.copy()
            for q in r:
                if res.get(q, None) is not None:
                    res[q] -= 1
            for j in res:
                if res[j] != 0:
                    k += 1
                    dec = True
                    break
            if dec is False:
                ar.append(k)
                k += 1

    return ar


#s = "barfoothefoobarman"
#arr = ["foo", "bar"]
s = "wordgoodgoodgoodbestword"
arr = ["word", "good", "best", "word"]
"barfoofoobarthefoobarman"
["bar", "foo", "the"]

print(s)

# arr = ["bb", "cc", "dd"]
print(check(arr, s))
