

def maxPairs(skillLevel, minDiff):
    # Write your code here
    skillLevel.sort()
    k = 0
    i = 1
    n = len(skillLevel)
    count = 0
    last = skillLevel[-1]
    while i < n:
        while i < n:
            if skillLevel[i] - skillLevel[k] >= minDiff:
                count += 1
                k += 1
                i += 1
                break
            i += 1
    return skillLevel, count


skillLevel = [1, 0]  # [2, 9, 0, 4, 2, 5, 6, 8, 1, 3, 9, 11, 10, 2, 7]
minDiff = 1
x, y = maxPairs(skillLevel, minDiff)
print(x, y)
