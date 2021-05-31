package main

import (
	"fmt"
	"strconv"
)

func main() {
	num := 123
	fmt.Println(numberToWords(num))

	num = 12345
	fmt.Println(numberToWords(num))

	num = 1234567891
	fmt.Println(numberToWords(num))
}

var numberMap = map[int]string{
	1: "One",
	2: "Two",
	3: "Three",
	4: "Four",
	5: "Five",
	6: "Six",
	7: "Seven",
	8: "Eight",
	9: "Nine",
}

var tensMap = map[int]string{
	1: "Ten",
	2: "Twenty",
	3: "Thirty",
	4: "Fourty",
	5: "Fifty",
	6: "Sixty",
	7: "Seventy",
	8: "Eighty",
	9: "Ninety",
}

func numberToWords(num int) string {
	numStr := strconv.Itoa(num)
	idx := len(numStr) - 1
	var billions string
	var millions string
	var thousands string
	var hundreds string

	// 2 147 483 647
	// 9 876 543 210 -> indices
	// length is up to 10

	// billions -> 10^9
	if idx == 9 {
		str, ok := numberMap[strToDigit(string(numStr[idx]))]
		if ok {
			billions = fmt.Sprintf("%s Billion", str)
		}
		idx--
	}

	// millions -> 10^6
	var mils int
	for ; idx >= 6; idx-- {
		mils *= 10
		mils += strToDigit(string(numStr[idx]))
	}
	milStr := hundredsToStr(mils)
	if milStr != "" {
		millions = fmt.Sprintf("%s Million", milStr)
	}

	// thousands -> 10^3
	var thou int
	for ; idx >= 3; idx-- {
		thou *= 10
		thou += strToDigit(string(numStr[idx]))
	}
	thouStr := hundredsToStr(mils)
	if thouStr != "" {
		thousands = fmt.Sprintf("%s Thousand", thouStr)
	}

	// hundreds -> 10^0
	var hund int
	for ; idx >= 0; idx-- {
		hund *= 10
		hund += strToDigit(string(numStr[idx]))
	}
	hundreds = hundredsToStr(hund)

	result := billions
	if result != "" && millions != "" {
		result += " "
	}
	result += millions
	if result != "" && thousands != "" {
		result += " "
	}
	result += thousands
	if result != "" && hundreds != "" {
		result += " "
	}
	result += hundreds

	return result
}

func strToDigit(str string) int {
	res, _ := strconv.Atoi(str)
	return res
}

func hundredsToStr(num int) string {
	// convert a number between 0 - 999 into a string
	numStr := strconv.Itoa(num)
	var hundreds string
	var tens string
	var ones string

	if len(numStr) >= 3 {
		hunds := strToDigit(string(numStr[2]))
		prefix, ok := numberMap[hunds]
		if ok {
			hundreds = fmt.Sprintf("%s Hundred", prefix)
		}
	}

	if len(numStr) >= 2 {
		tns := strToDigit(string(numStr[1]))
		word, ok := tensMap[tns]
		if ok {
			tens = word
		}
	}

	ons := strToDigit(string(numStr[0]))
	word, ok := numberMap[ons]
	if ok {
		ones = word
	}

	result := hundreds
	if result != "" && tens != "" {
		result += " "
	}
	result += tens
	if result != "" && ones != "" {
		result += " "
	}
	result += ones

	return result
}
