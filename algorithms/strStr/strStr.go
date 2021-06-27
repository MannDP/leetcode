package main

import "fmt"

func main() {
	fmt.Println(strStr("hello", "ll"))
	fmt.Println(strStr("aaaaa", "bba"))
	fmt.Println(strStr("", ""))
}

func strStr(haystack string, needle string) int {
	// special case
	if needle == "" {
		return 0
	}

	for hidx := range haystack {
		matched := 0
		for range needle {
			hloc := hidx + matched
			if hloc < len(haystack) && haystack[hloc] == needle[matched] {
				matched++
			} else {
				break
			}

			if matched == len(needle) {
				return hidx
			}
		}
	}

	return -1
}
