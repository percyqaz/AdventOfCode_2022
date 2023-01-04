file = open("test_data.txt")
data = file.read().replace("\r","").split("\n")
file.close()

up = []
down = []
left = []
right = []

height = len(data) - 2
width = len(data[0]) - 2

START = (0, -1)
END = (width - 1, height)

distances = {}
distances[START] = [0]

y = 0
for line in data[1:-1]:
    for x in range(0, len(line) - 2):
        if line[x + 1] == ">": right.append((x, y))
        elif line[x + 1] == "<": left.append((x, y))
        elif line[x + 1] == "v": down.append((x, y))
        elif line[x + 1] == "^": up.append((x, y))
    y += 1
    
def position_empty(pos, time):
    x, y = pos
    for a, b in up:
        if x == a and y == (b - time) % height:
            return False
    for a, b in down:
        if x == a and y == (b + time) % height:
            return False
    for a, b in left:
        if x == (a - time) % width and y == b:
            return False
    for a, b in right:
        if x == (a + time) % width and y == b:
            return False
    return True
    
check_next = [{ "position": (0, -1), "time": 0 }]
            
def explore(pos, time):
    global check_next
    x, y = pos
    
    if pos != END and pos != START:
        if x >= width or x < 0 or y < 0 or y >= height: return
    elif pos == END:
        print("final answer:", time)
        
    if position_empty(pos, time):
        if pos not in distances: distances[pos] = []
        if time not in distances[pos]:
            distances[pos].append(time)
            check_next.append({"position": pos, "time": time })

while check_next and not (END in distances):
    
    next = check_next.pop(0)
    
    time = next["time"]
    position = next["position"]
    
    x, y = position
    explore((x - 1, y), time + 1)
    explore((x + 1, y), time + 1)
    explore((x, y - 1), time + 1)
    explore((x, y + 1), time + 1)
    explore((x, y), time + 1)

for y in range(height):
    for x in range(width):
        try: print(";".join(map(str,distances[(x, y)])).ljust(5), end="")
        except KeyError: print("---".ljust(5), end="")
    print("")