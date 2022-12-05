use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::vec::Vec;
use std::collections::LinkedList;

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() {

	let mut stack_info : Vec<String> = Vec::new();
	let mut stacks : Vec<LinkedList<String>> = Vec::new();
	let mut collecting_stack_info = true;

	if let Ok(lines) = read_lines("test_data.txt") {
		for line in lines {

			let line = line.unwrap();

			// THIS SECTION PARSES THE STATE OF THE STACKS (TRIGGERS ON A BLANK LINE)
			if line == "" {
				collecting_stack_info = false;

				let number_of_stacks = (stack_info.pop().unwrap().len() + 1) / 4;

				for _ in 0..number_of_stacks {
					stacks.push(LinkedList::new());
				}

				while !stack_info.is_empty() {
					let current_line = stack_info.pop().unwrap();

					for n in 0..number_of_stacks {
						// This is literally slicing bytes, and only works because of the characters used
						let item : String = current_line.get(4* n + 1 .. 4 * n + 2).unwrap().to_string();
						if item != " " { stacks[n].push_front(item); }
					}
				}

				println!("Starting off, top of stacks reads:");
				for n in 0..number_of_stacks {
					println!("{}: {}", (n+1), stacks[n].front().unwrap());
				}
			}

			else if collecting_stack_info {
				stack_info.push(line);
			}

			// THIS SECTION MOVES BOXES AROUND BASED ON THE INSTRUCTION
			else {
				let split : Vec<&str> = line.split_whitespace().collect();

				let amount = split[1].to_string().parse::<usize>().unwrap();
				let from_stack = split[3].to_string().parse::<usize>().unwrap() - 1;
				let to_stack = split[5].to_string().parse::<usize>().unwrap() - 1;

				for _ in 0..amount {
					let moved_item = stacks[from_stack].pop_front().unwrap();
					stacks[to_stack].push_front(moved_item);
				}
			}
		}

		// PRINT STATE OF THE STACKS
		println!("At the end, top of stacks reads:");
		for stack in stacks {
			println!("{}", stack.front().unwrap());
		}
	}
}