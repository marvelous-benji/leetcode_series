package main

import "fmt"

func is_pair_anagram(str1, str2 string) {
	map1 := make(map[string]int)
	map2 := make(map[string]int)

	if len(str1) != len(str2) {
		fmt.Println(false)
		return
	}
	for id, val := range str1 {
		_, ok := map1[string(val)]
		if ok {
			map1[string(val)] += 1
		} else {
			map1[string(val)] = 1
		}
		_, ok = map2[string(str2[id])]
		if ok {
			map2[string(str2[id])] += 1
		} else {
			map2[string(str2[id])] = 1
		}
	}
	for key, _ := range map1 {
		_, ok := map2[key]
		if ok {
			if map1[key] != map2[key] {
				fmt.Println(false)
				return
			}
		} else {
			fmt.Println(false)
			return
		}
	}
	fmt.Println(true)
	return
}

func main() {
	is_pair_anagram("hard work pay's off", "pay's off hard work")
}
