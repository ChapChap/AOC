package math

/*MinMax return min and max of an array
 */
func MinMax(a []int) (min int, max int) {
	min = a[0]
	max = a[0]
	for _, value := range a {
		if value < min {
			min = value
		}
		if value > max {
			max = value
		}
	}
	return min, max
}

/*MinMaxIndexes return indexes of min and max of an array
 */
func MinMaxIndexes(a []int) (min int, max int) {
	min = 0
	max = 0
	for i, value := range a {
		if value < a[min] {
			min = i
		}
		if value > a[max] {
			max = i
		}
	}
	return min, max
}
