file = open("test_data.txt")
lines = file.readlines()
file.close()

monkeys = {}
memo = {}

for line in lines:
    s1 = line.strip().split(":")
    name = s1[0]
    shout = s1[1].split()
    if name == "root":
        root = shout
    else: monkeys[name] = shout

del monkeys["humn"]

def monkey(id):
    if id in memo: return memo[id]

    shout = monkeys[id]
    if len(shout) == 1:
        result = int(shout[0])
        memo[id] = result
        return result

    left = monkey(shout[0])
    right = monkey(shout[2])
    op = shout[1]
    if op == "+":
        result = left + right
        memo[id] = result
        return result
    elif op == "-":
        result = left - right
        memo[id] = result
        return result
    if op == "*":
        result = left * right
        memo[id] = result
        return result
    if op == "/":
        result = left / right
        memo[id] = result
        return result

target = monkey(root[2])
print(target)

lo = 0
hi = 1000000000000000000

while True:
    test = (lo + hi) / 2.0
    memo = { "humn": test }

    result = monkey(root[0])
    print(test, result, result - target)
    if result < target:
        hi = test
    else: lo = test
