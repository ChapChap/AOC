package main

// Res1 : 228
// Res2 : 6818112000

import (
	"AOC/utils/files"
)

func main() {
	input := files.ImportInput("input")
	// Part 1
	println("res1:", countTreesEncountered(3, 1, input))
	// Part 2
	var slopes = [][]int{{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}}
	var res int = 1
	for _, slope := range slopes {
		res *= countTreesEncountered(slope[0], slope[1], input)
	}
	println("res2:", res)
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
