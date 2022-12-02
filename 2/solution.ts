import * as fs from 'fs';

let lines = fs.readFileSync("./test_data.txt", "utf-8").split("\n");

var choice_score = 0;
var win_score = 0;

for (var line of lines) {
	switch(line.trim()) {
			case "A X": choice_score += 1; win_score += 3; break; // rock <- rock
			case "A Y": choice_score += 2; win_score += 6; break; // rock <- paper
			case "A Z": choice_score += 3; win_score += 0; break; // rock <- scissors
			
			case "B X": choice_score += 1; win_score += 0; break; // paper <- rock
			case "B Y": choice_score += 2; win_score += 3; break; // paper <- paper
			case "B Z": choice_score += 3; win_score += 6; break; // paper <- scissors
			
			case "C X": choice_score += 1; win_score += 6; break; // scissors <- rock
			case "C Y": choice_score += 2; win_score += 0; break; // scissors <- paper
			case "C Z": choice_score += 3; win_score += 3; break; // scissors <- scissors
			default: console.log(line); break;
	}
}

const score = choice_score + win_score;
console.log(score)