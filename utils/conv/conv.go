package conv

import (
	"strconv"
)

/*ToIntSlice go
 */
func ToIntSlice(slice []string) []int {
	sliceToReturn := []int{}

	for _, current := range slice {
		convertedString, err := strconv.Atoi(current)

		if err != nil {
			panic(err)
		}

		sliceToReturn = append(sliceToReturn, convertedString)
	}

	return sliceToReturn
}

/*ToInt go
 */
func ToInt(str string) int {
	number, err := strconv.Atoi(str)

	if err != nil {
		panic(err)
	}

	return number
}

/*InputToInt go
 */
func InputToInt(input []string) []int {
	var list []int
	for _, line := range input {
		i, err := strconv.Atoi(line)
		if err != nil {
			panic(err)
		} else {
			list = append(list, i)
		}
	}
	return list
}
