from collections import defaultdict


map1 = defaultdict(int)
map2 = defaultdict(int)


def is_pair_anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    
    for id,chr in enumerate(str1):
        map1[chr] += 1
        map2[str2[id]] += 1

    for element in map1:
        if map1[element] != map2[element]:
            return False
    return True



def main():
    result = is_pair_anagram('bav credit','debit card')
    print(result)


main()