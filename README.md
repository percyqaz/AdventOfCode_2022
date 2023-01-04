# Advent of Code 2022
https://adventofcode.com/ is an event where every day for 25 days leading up to christmas, you get a challenge that should be solved using programming or similar tools.  

My original goal was to use this as an excuse to use **a different tool or language each day**, some for the first time ever.  

#### Day 15 note

Now that the problems have ramped up in difficulty (day 15 onwards), **I will be freely using the most comfortable tools at my disposal**.  
(Perhaps still with a few surprises)

#### Day 25 note

I didn't do the puzzle every day after the 16th because I was doing christmas things :) But am pleased to have followed up and finished what I started

By the end the puzzles got easier (in my opinion) so I could've gotten creative with languages again -- See you next year!

----

Don't look at any of the solutions if you don't want spoilers!

All solutions have been my own with basically 0 outside assistance (Once or twice a meme from the subreddit would spark inspiration)

----

## My thoughts on some languages after using them for challenges

### Rust
Really liked the error messages, they helped teach me the language and also pointed out some memory safety issues I'd never thought about before.  
Took a long time to write as a first timer but I can see myself using it for general purposes

Would probably recommend you try Rust at least once based on this experience

### Haskell
Long time returner after learning it at university (and using it for a few rhythm game project scripts at some point)  

First off installing it on Windows has gotten somewhat worse (But I appreciate `haskell-stack` being available and doing all I needed and more)  

Second off writing the solution drove me absolutely insane despite knowing exactly what the code would need to look like in Haskell form  
Type errors everywhere, accidentally using the wrong symbols (`::` instead of `:`, `+` instead of `++`) because of F# habits  
By the time it compiled I had a correct solution which made me feel big brained though

### Regex
I sensed that day 6 was doable using regex tooling and evilly cackled when I was right.  
You can do anything you want with Regex if you put your mind to it (and find an implementation with the right features)

### OCaml
Also long time returning after learning it at university for compilers  

I spent 2 hours installing the toolchain on windows, only for the basic compiler to
- Give nothing more informative than "syntax error" 90% of the time
- Highlight the wrong part of the line due to not considering whitespace in its positions, but displaying the line with the whitespace
- Cause me to spend 2 more hours on what was a simple nested loop task

I even use a direct descendant of this language every day - F#

Would strongly recommend F# over older MLs based on this experience

### Scala
Opinion: Overall quite good  
I didn't like eliding () on 0-arity functions before, but after looking more closely at the conventions and how it's implemented, it's pretty sensible

### Go
Opinion: Not very enthused  
The language appears to build on C in many ways with some good ideas, however they only make sense if you program a lot of C (I don't)  
Call me a nerd but I prefer Rust's improvements on C on all fronts (syntax, memory safety, type safety)

----

Some languages ~~I'm trying to eventually work in~~ to use next year (the more impractical the better):
- Prolog
- Elixir
- Kotlin <- might not happen if I can't get the tooling to work
- Bash
- Clojure/Scheme/Common Lisp/Racket/T <- might not happen if I can't get the tooling to work
