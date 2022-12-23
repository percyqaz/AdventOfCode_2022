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
    return #comment this line for debug
    print("*-------*")
    for row in range(1, 20):
        print("|", end="")
        for column in range(1, 8):
            if (column, row) in points: print("#", end="")
            elif (column - x, row - y) in block: print("@", end="")
            else: print(".", end="")
        print("|")
    input()


for i in range(2022):

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

    visualise(x, y, block["contents"], points)

    while True:

        # horizontal movement
        if flow[flow_index] == ">":
            x += 1
            if collision(x, y, block["contents"], points): x -= 1
        else:
            x -= 1
            if collision(x, y, block["contents"], points): x += 1
        visualise(x, y, block["contents"], points)
        flow_index = (flow_index + 1) % len(flow)

        # vertical movement
        y -= 1
        if collision(x, y, block["contents"], points):
            y += 1

            for a, b in block["contents"]:
                points.add((x + a, y + b))
                if y + b > height: height = y + b
            break
        visualise(x, y, block["contents"], points)

    # next loop
    block_index = (block_index + 1) % len(blocks)

print(height)
