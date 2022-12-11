type MonkeyOperand =
    | It
    | Number of int
    member this.Evaluate(old: bigint) =
        match this with
        | It -> old
        | Number i -> bigint i

type MonkeyOperation =
    | Times of MonkeyOperand * MonkeyOperand
    | Add of MonkeyOperand * MonkeyOperand
    member this.Evaluate(old: bigint) =
        match this with
        | Times (a, b) -> a.Evaluate old * b.Evaluate old
        | Add (a, b) -> a.Evaluate old + b.Evaluate old

type Monkey = 
    {
        Items: ResizeArray<bigint>
        Operation: MonkeyOperation
        Test: bigint
        IfTrue: int
        IfFalse: int
        mutable Inspections: bigint
    }

module Reader =
    
    open System.IO

    let mutable magic_optimisation_number = 1I

    let mutable allText = File.ReadAllText("test_data.txt")

    let expect(string: string) =
        let split : string[] = allText.Split([|string|], 2, System.StringSplitOptions.TrimEntries)
        assert(split.[0] = string)
        allText <- split.[1]

    let until(string: string) =
        let split : string[] = allText.Split([|string|], 2, System.StringSplitOptions.TrimEntries)
        allText <- try string + split.[1] with _ -> ""
        split[0]

    let restOfLine() = until "\n"

    let parse_operand (o: string) : MonkeyOperand = if o = "old" then It else int o |> Number

    let parse_operation (op: string) : MonkeyOperation =
        if op.Contains("*") then
            let split = op.Split("*", System.StringSplitOptions.TrimEntries)
            Times (parse_operand split.[0], parse_operand split.[1])
        else
            let split = op.Split("+", System.StringSplitOptions.TrimEntries)
            Add (parse_operand split.[0], parse_operand split.[1])

    let parse_monkey() : Monkey =
        expect "Monkey"
        until ":" |> printfn "Parsing monkey %s"
        expect "Starting items:"
        let startingItems = 
            restOfLine()
            |> fun s -> s.Split(",", System.StringSplitOptions.TrimEntries)
            |> Array.map int
            |> Array.map bigint
            |> ResizeArray
        expect "Operation: new ="
        let operation = restOfLine() |> parse_operation
        expect "Test: divisible by"
        let test = restOfLine() |> int |> bigint
        magic_optimisation_number <- magic_optimisation_number * test
        expect "If true: throw to monkey"
        let if_true = restOfLine() |> int
        expect "If false: throw to monkey"
        let if_false = restOfLine() |> int
        
        { Items = startingItems; Operation = operation; Test = test; IfTrue = if_true; IfFalse = if_false; Inspections = 0I }

    let parse() : Monkey[] =
        let monkeys = ResizeArray<Monkey>()
        while allText <> "" do
            let monkey = parse_monkey()
            printfn "Parsed monkey: %A" monkey
            monkeys.Add(monkey)
        Array.ofSeq monkeys

module Solution =

    let monkeys = Reader.parse()

    let round(i: int) =
        for m in monkeys do
            m.Inspections <- m.Inspections + bigint m.Items.Count
            while m.Items.Count > 0 do
                let worry_level = m.Items.[0]
                m.Items.RemoveAt 0

                let new_worry_level = m.Operation.Evaluate(worry_level)
                let after_inspection = new_worry_level % Reader.magic_optimisation_number

                if after_inspection % m.Test = 0I then
                    monkeys.[m.IfTrue].Items.Add(after_inspection)
                else monkeys.[m.IfFalse].Items.Add(after_inspection)
        //printfn "After round %i" i
        //for i, m in Array.indexed monkeys do
        //    printfn "Monkey %i: %s" i (m.Items |> Seq.map string |> String.concat ", ")

    let main() =
        for i = 1 to 10000 do round(i)
        monkeys
        |> Array.map (fun monkey -> monkey.Inspections)
        |> Array.sortDescending
        //|> fun x -> printfn "%A" x; x
        |> fun xs -> xs.[1] * xs.[0]
        |> printfn "Monkey business: %O"

Solution.main()
