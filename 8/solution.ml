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
	
let left () =
	for y = 0 to height - 1 do
		let h : int ref = ref (-1) in
		for x = 0 to width - 1 do
			let treec : char = (List.nth lines y).[x] in 
			let tree : int = treec |> String.make 1 |> int_of_string in
			if tree > !h then
				begin
				h := tree;
				Array.set (Array.get markers y) x true;
				end;
		done;	
	done ;;
	
let top () =
	for x = 0 to width - 1 do
		let h : int ref = ref (-1) in
		for y = 0 to height - 1 do
			let treec : char = (List.nth lines y).[x] in 
			let tree : int = treec |> String.make 1 |> int_of_string in
			if tree > !h then
				begin
				h := tree;
				Array.set (Array.get markers y) x true;
				end;
		done;	
	done ;;
	
let right () =
	for y = 0 to height - 1 do
		let h : int ref = ref (-1) in
		for x = width - 1 downto 0 do
			let treec : char = (List.nth lines y).[x] in 
			let tree : int = treec |> String.make 1 |> int_of_string in
			if tree > !h then
				begin
				h := tree;
				Array.set (Array.get markers y) x true;
				end;
		done;	
	done ;;
	
let bottom () =
	for x = 0 to width - 1 do
		let h : int ref = ref (-1) in
		for y = height - 1 downto 0 do
			let treec : char = (List.nth lines y).[x] in 
			let tree : int = treec |> String.make 1 |> int_of_string in
			if tree > !h then
				begin
				h := tree;
				Array.set (Array.get markers y) x true;
				end;
		done;	
	done ;;
	
let count () =
	let c : int ref = ref 0 in
	for y = 0 to height - 1 do
		for x = 0 to width - 1 do
			if Array.get (Array.get markers y) x then
				c := !c + 1;
		done;
	done;
	!c ;;

let () = 
	left ();
	top ();
	right ();
	bottom ();
	printf "%i\n" (count ()) ;;