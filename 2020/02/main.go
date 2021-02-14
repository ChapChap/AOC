package main

import (
	"AOC/utils/conv"
	"AOC/utils/files"
	"errors"
	"strings"
)

/*Policy type conatins min and max occurence of a letter
 */
type Policy struct {
	min, max int
	letter   string
}

func main() {
	input := files.ImportInput("input")
	println(countValidPasswords(input))
}

func getPasswordAndPolicy(str string) (string, Policy) {
	split := strings.Split(str, ": ")
	if len(split) != 2 {
		panic(errors.New("Invalid input type"))
	} else {
		var password = split[1]
		var rawPolicy = strings.Split(strings.ReplaceAll(split[0], "-", " "), " ")
		if len(rawPolicy) != 3 {
			panic(errors.New("Invalid input type"))
		} else {
			var policy = Policy{
				min:    conv.ToInt(rawPolicy[0]),
				max:    conv.ToInt(rawPolicy[1]),
				letter: rawPolicy[2],
			}
			return password, policy
		}
	}
}

func isValidPassword(password string, policy Policy) bool {
	occurence := strings.Count(password, policy.letter)
	if occurence >= policy.min && occurence <= policy.max {
		return true
	} else {
		return false
	}
}

func countValidPasswords(list []string) int {
	var count int
	for i := 0; i < len(list); i++ {
		line := list[i]
		if isValidPassword(getPasswordAndPolicy(line)) {
			count++
		}
	}
	return count
}
