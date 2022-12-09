import scala.io.Source
import scala.io.StdIn.readLine

class Knot() {
	
	private var tail : Option[Knot] = None
	
	var x = 0
	var y = 0
	
	def with_tail = {
		val new_tail = new Knot()
		tail = Some(new_tail)
		new_tail
	}
	
	def follow(head_x: Int, head_y: Int) : Unit = {
		if (head_x - x == 2 && head_y - y == 2) {
			x += 1
			y += 1
			move_tail
		}
		else if (x - head_x == 2 && head_y - y == 2) {
			x -= 1
			y += 1
			move_tail
		}
		else if (head_x - x == 2 && y - head_y == 2) {
			x += 1
			y -= 1
			move_tail
		}
		else if (x - head_x == 2 && y - head_y == 2) {
			x -= 1
			y -= 1
			move_tail
		}
		else if (head_x - x == 2) {
			x += 1
			y = head_y
			move_tail
		}
		else if (x - head_x == 2) {
			x -= 1
			y = head_y
			move_tail
		}
		else if (head_y - y == 2) {
			y += 1
			x = head_x
			move_tail
		}
		else if (y - head_y == 2) {
			y -= 1
			x = head_x
			move_tail
		}
	}
	
	def move_tail = {
		tail match {
			case Some(t) => t.follow(x, y)
			case None => ()
		}
	}
	
	def left = { x -= 1; move_tail }
	
	def right = { x += 1; move_tail }
	
	def up = { y -= 1; move_tail }
	
	def down = { y += 1; move_tail }
	
}
	
object AOCDay9 {

	var rope = new Knot()
	var end_of_rope = rope.with_tail.with_tail.with_tail.with_tail.with_tail.with_tail.with_tail.with_tail.with_tail
	
	var locations = List[String]()
	
	def mark_location = {
		locations = s"${end_of_rope.x}, ${end_of_rope.y}" :: locations
	}

	def main(args : Array[String]) = {
		val lines = Source.fromFile("test_data.txt").getLines.toArray
		
		mark_location
		
		for (line <- lines) {
			val split = line.split(" ")
			val direction = split(0)
			val count = split(1).toInt
			
			if (direction == "L") {
				for (i <- 1 to count) { rope.left; mark_location }
			}
			
			if (direction == "R") {
				for (i <- 1 to count) { rope.right; mark_location }
			}
			
			if (direction == "D") {
				for (i <- 1 to count) { rope.down; mark_location }
			}
			
			if (direction == "U") {
				for (i <- 1 to count) { rope.up; mark_location }
			}
		}
		
		println(locations.distinct.length)
	}
}