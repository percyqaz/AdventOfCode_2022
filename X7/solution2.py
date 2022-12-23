file = open("blocks.txt")
data = file.read()
file.close()

block_text = data.replace("\r", "").split("\n\n")

blocks = []

for b in block_text:
    lines = b.strip().split("\n")
    block = []
    width = len(lines[0])
    height = len(lines)
    for y in range(height):
        for x in range(width):
            if lines[y][x] == "#":
                block.append((x, y))
    blocks.append({ "contents": block, "height": height })

file = open("test_data.txt")
flow = file.read().strip()
file.close()

block_index = 0
flow_index = 0
points = set()
height = 0

def visualise(x, y, block, points):
    #return #comment this line for debug
    for row in range(height - 10, height + 10):
        print("|", end="")
        for column in range(1, 8):
            if (column, row) in points: print("#", end="")
            elif (column - x, row - y) in block: print("@", end="")
            else: print(".", end="")
        print("|")
    input()

i = 0
offset = 0
patterns = {}

print("identifying period of pattern...")

target = 1000000000000

while True:

    if offset == 0 and (block_index, flow_index) in patterns:
        at, height_at = patterns[(block_index, flow_index)]
        print("found period at", at, "length", i - at, "height", height - height_at)
        period = i - at
        if (target - i) % period == 0:
            reps = (target - i) // period
            print("period goes into what's left", reps, "times")
            i += reps * period
            print("..", i)
            offset = reps * (height - height_at)
    patterns[(block_index, flow_index)] = (i, height)

    if i % 10000 == 0: print("..", i)

    if i >= target: break

    def collision(x, y, block, points):
        for a, b in block:
            if y + b <= 0: return True
            elif x + a <= 0: return True
            elif x + a >= 8: return True
            elif ((x + a), (y + b)) in points: return True
        return False

    # appear rock
    block = blocks[block_index]
    x = 3
    y = height + 4

    while True:

        # horizontal movement
        if flow[flow_index] == ">":
            x += 1
            if collision(x, y, block["contents"], points): x -= 1
        else:
            x -= 1
            if collision(x, y, block["contents"], points): x += 1
        flow_index = (flow_index + 1) % len(flow)

        # vertical movement
        y -= 1
        if collision(x, y, block["contents"], points):
            y += 1

            for a, b in block["contents"]:
                points.add((x + a, y + b))
                if y + b > height: height = y + b
            break

    # next loop
    block_index = (block_index + 1) % len(blocks)
    i += 1

    print("height after", i, "rocks:", height + offset)

print(height + offset)
#1564431486885
