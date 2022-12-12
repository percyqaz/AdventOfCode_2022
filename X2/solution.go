package main

import (
    "bufio"
    "fmt"
    "os"
)

type Position struct {
	X, Y int
}

type Tile struct {
	Height int
	Active bool
	Distance int
}

func (t *Tile) Explore(h int, d int) {
	if h >= t.Height - 1 && d < t.Distance {
		t.Distance = d
		t.Active = true
	}
}

func (t *Tile) Explored() {
	t.Active = false
}

func load_lines() (lines []string) {
	lines = []string{}
	
    file, _ := os.Open("test_data.txt")
    defer file.Close()
	
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
	return
}

func load_grid(lines []string) (grid [][]Tile, start Position, end Position) {
	
	grid = make([][]Tile, len(lines))
	for y := range grid {
		grid[y] = make([]Tile, len(lines[0]))
	}
	
	for y := 0; y < len(lines); y++ {
		for x := 0; x < len(lines[y]); x++ {
			c := lines[y][x]
			if c == 'S' {
				start = Position{x, y}
				grid[y][x] = Tile{0, true, 0}
			} else if c == 'E' {
				end = Position{x, y}
				grid[y][x] = Tile{25, false, 99999}
			} else {
				grid[y][x] = Tile{int(c - 'a'), false, 99999}
			}
		}		
	}
	
	return
}

func pass(grid [][]Tile) {
	w := len(grid[0])
	h := len(grid)
	
	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			tile := grid[y][x]
			if (tile.Active) {
				if y > 0 {
					grid[y - 1][x].Explore(tile.Height, tile.Distance + 1)
				}
				if y < h - 1 {
					grid[y + 1][x].Explore(tile.Height, tile.Distance + 1)
				}
				if x > 0 {
					grid[y][x - 1].Explore(tile.Height, tile.Distance + 1)
				}
				if x < w - 1 {
					grid[y][x + 1].Explore(tile.Height, tile.Distance + 1)
				}
				grid[y][x].Explored()
			}
		}
	}
}

func display(grid [][]Tile) (result string) {
	result = ""
	
	w := len(grid[0])
	h := len(grid)
	
	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			tile := grid[y][x]
			if tile.Active {
				result = result + "*"
			} else if tile.Distance < 99999 {
				result = result + "."
			} else {
				result = result + " "
			}
		}
		result = result + "\n"
	}
	
	return
}

func main() {

	lines := load_lines()
	grid, _, end := load_grid(lines)
	
	for {
		pass(grid)
		
		fmt.Printf("%s", display(grid))
		fmt.Printf("%v", grid[end.Y][end.X].Distance)
		
		reader := bufio.NewReader(os.Stdin)
		reader.ReadString('\n')
	}
}