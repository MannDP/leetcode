package main

import "fmt"

func main() {
	fmt.Println(rob([]int{1, 2, 3, 1}))
}

func rob(nums []int) int {
	oneBehind := 0
	twoBehind := 0

	for _, value := range nums {
		with := twoBehind + value
		without := oneBehind

		twoBehind = oneBehind
		oneBehind = with
		if without > oneBehind {
			oneBehind = without
		}

	}

	return oneBehind
}
