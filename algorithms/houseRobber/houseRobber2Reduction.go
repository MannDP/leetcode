package main

import "fmt"

func main() {
	tc := []int{1}
	fmt.Println(rob(tc))
}

func rob(nums []int) int {
	var result int

	if len(nums) == 0 {
		return 0
	}

	// slicing fun
	if len(nums) == 1 {
		return nums[0]
	}

	result = rob1(nums[:len(nums)-1])

	if len(nums) > 1 {
		withLast := rob1(nums[1:])
		if withLast > result {
			result = withLast
		}
	}

	return result
}

func rob1(nums []int) int {
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
