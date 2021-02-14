package main

import "AOC/utils/files"

func main() {
	input := files.ImportInput("input")
	println("res:", countTreesEncountered(3, 1, input))
}

func countTreesEncountered(a int, b int, m []string) int {
	rows := len(m)
	columns := len(m[0])
	var count int = 0
	for i, j := 0, 0; i < columns && j < rows; i, j = (i+a)%columns, j+b {
		if isTree(i, j, m) {
			count++
		}
	}
	return count
}

func isTree(x int, y int, m []string) bool {
	return string(m[y][x]) == "#"
}
