open Printf

let read_file filename = 
	let lines = ref [] in
	let chan = open_in filename in
	try
	  while true; do
		lines := input_line chan :: !lines
	  done;
	  !lines
	with End_of_file ->
	  close_in chan;
	  List.rev !lines ;;

let lines : string list = read_file "test_data.txt" ;;

let width = lines |> List.hd |> String.length ;;
let height = lines |> List.length ;;

let markers = Array.make_matrix width height false ;;

let rec print_lines xs =
	match xs with
	| [] -> ();
	| x :: xs -> print_endline x; print_lines xs ;;
	
let rate_this_tree a b =

	let this_tree = (List.nth lines b).[a] |> String.make 1 |> int_of_string in
	let product = ref 1 in
	
	(* right *)
	let blocked = ref false in
	let count = ref 0 in
	for x = a + 1 to width - 1 do
		let treec : char = (List.nth lines b).[x] in 
		let tree : int = treec |> String.make 1 |> int_of_string in
		if Bool.not (!blocked) then count := !count + 1;
		if tree >= this_tree then blocked := true;
	done;
	product := !product * !count;
	(* left *)
	let blocked = ref false in
	let count = ref 0 in
	for x = a - 1 downto 0 do
		let treec : char = (List.nth lines b).[x] in 
		let tree : int = treec |> String.make 1 |> int_of_string in
		if Bool.not (!blocked) then count := !count + 1;
		if tree >= this_tree then blocked := true;
	done;
	product := !product * !count;
	(* up *)
	let blocked = ref false in
	let count = ref 0 in
	for y = b - 1 downto 0 do
		let treec : char = (List.nth lines y).[a] in 
		let tree : int = treec |> String.make 1 |> int_of_string in
		if Bool.not (!blocked) then count := !count + 1;
		if tree >= this_tree then blocked := true;
	done;
	product := !product * !count;
	(* down *)
	let blocked = ref false in
	let count = ref 0 in
	for y = b + 1 to height - 1 do
		let treec : char = (List.nth lines y).[a] in 
		let tree : int = treec |> String.make 1 |> int_of_string in
		if Bool.not (!blocked) then count := !count + 1;
		if tree >= this_tree then blocked := true;
	done;
	product := !product * !count;
	
	!product ;;
	
let best_tree () =
	let best : int ref = ref 0 in
	for y = 0 to height - 1 do
		for x = 0 to width - 1 do
			let tree_rating = rate_this_tree x y in
			if tree_rating > !best then
				best := tree_rating;
		done;
	done;
	!best ;;

let () = 
	printf "%i\n" (best_tree ()) ;;