package main

// Res1 : 121396
// Res2 : 73616634

import (
	"AOC/utils/conv"
	"AOC/utils/files"
	"errors"
	"fmt"
)

func main() {
	input := files.ImportInput("input")
	list := conv.InputToInt(input)

	res, err := isSum(list, 3, 2020)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("res:", res)
	}
}

func isSum(list []int, members int, total int) (int, error) {
	switch members {
	case 2:
		return isSum2(list, total)
	case 3:
		return isSum3(list, total)
	default:
		return 0, errors.New("Sum members must be 2 or 3")
	}
}

func isSum2(list []int, total int) (int, error) {
	for i := 0; i < len(list); i++ {
		for j := 0; j < len(list); j++ {
			if list[i]+list[j] == total {
				return list[i] * list[j], nil
			}
		}
	}
	return 0, errors.New("No matching found")
}

func isSum3(list []int, total int) (int, error) {
	for i := 0; i < len(list); i++ {
		for j := 0; j < len(list); j++ {
			for k := 0; k < len(list); k++ {
				if list[i]+list[j]+list[k] == total {
					return list[i] * list[j] * list[k], nil
				}
			}
		}
	}
	return 0, errors.New("No matching found")
}
