import scala.io.Source
import scala.io.StdIn.readLine

object AOCDay9 {

	var head_x = 0
	var head_y = 0
	var tail_x = 0
	var tail_y = 0
	
	var locations = List[String]()
	
	def left = {
		head_x -= 1
		if (tail_x - head_x == 2) { tail_x = head_x + 1; tail_y = head_y }
	}
	
	def right = {
		head_x += 1
		if (head_x - tail_x == 2) { tail_x = head_x - 1; tail_y = head_y }
	}
	
	def up = {
		head_y -= 1
		if (tail_y - head_y == 2) { tail_y = head_y + 1; tail_x = head_x }
	}
	
	def down = {
		head_y += 1
		if (head_y - tail_y == 2) { tail_y = head_y - 1; tail_x = head_x }
	}
	
	def mark_location = {
		locations = s"${tail_x}, ${tail_y}" :: locations
	}

	def main(args : Array[String]) = {
		val lines = Source.fromFile("test_data.txt").getLines.toArray
		
		mark_location
		
		for (line <- lines) {
			val split = line.split(" ")
			val direction = split(0)
			val count = split(1).toInt
			
			if (direction == "L") {
				for (i <- 1 to count) { left; mark_location }
			}
			
			if (direction == "R") {
				for (i <- 1 to count) { right; mark_location }
			}
			
			if (direction == "D") {
				for (i <- 1 to count) { down; mark_location }
			}
			
			if (direction == "U") {
				for (i <- 1 to count) { up; mark_location }
			}
		}
		
		println(locations.distinct.length)
	}
}