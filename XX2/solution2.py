file = open("test_data.txt")
data = str(file.read()).replace("\r","")
file.close()

split = data.split("\n\n")
map_blob = split[0]
path = split[1]

path_parts = []
while "L" in path or "R" in path:
    l = path.find("L")
    r = path.find("R")
    if r > 0 and (r < l or l < 0):
        s = path.split("R")
        path_parts.append(int(s[0]))
        path_parts.append("R")
        path = "R".join(s[1:])
    else:
        s = path.split("L")
        path_parts.append(int(s[0]))
        path_parts.append("L")
        path = "L".join(s[1:])
        
path_parts.append(int(path))

map_lines = map_blob.split("\n")
height = len(map_lines)
width = 0
for l in map_lines:
    width = max(width, len(l))
    
map = []
   
for y in range(height):
    line = []
    for x in range(width):
        try:
            line.append(map_lines[y][x])
        except:
            line.append(' ')
    map.append(line)
    
def region(x, y):
    return (x * 3 // width, y * 4 // height)
    
def in_region(x, y):
    return (x % (width // 3), y % (height // 4))

def left_edge(region, coord):
    x, y = region
    return (x * width // 3, y * height // 4 + coord)
    
def right_edge(region, coord):
    x, y = region
    return ((x + 1) * width // 3 - 1, y * height // 4 + coord)

def bottom_edge(region, coord):
    x, y = region
    return (x * width // 3 + coord, (y + 1) * height // 4 - 1)
    
def top_edge(region, coord):
    x, y = region
    return (x * width // 3 + coord, y * height // 4)
            
            
"""
 EF                 E        D
 D                 BDF      BCF
BC                  C        A
A
"""

A = (0, 3)
B = (0, 2)
C = (1, 2)
D = (1, 1)
E = (1, 0)
F = (2, 0)
            
x, y = left_edge(E, 0)
facing = 0 # right, 1 = down, 2 = left, 3 = up

BLOCKSIZE = width // 3

right = {}
    
for move in path_parts:
    if move == "L":
        facing -= 1
        facing %= 4
    elif move == "R":
        facing += 1
        facing %= 4
    else:
        for i in range(move):
            next_facing = facing
            # RIGHT
            if facing == 0:
                next_x = x + 1
                next_y = y
                if next_x >= width or map[next_y][next_x] == " ":
                    current_region = region(x, y)
                    rx, ry = in_region(x, y)
                    if current_region == A:
                        next_facing = 3
                        next_x, next_y = bottom_edge(C, ry)
                        print("A -> C")
                    elif current_region == C:
                        next_facing = 2
                        next_x, next_y = right_edge(F, BLOCKSIZE - 1 - ry)
                        print("C -> F")
                    elif current_region == F:
                        next_facing = 2
                        next_x, next_y = right_edge(C, BLOCKSIZE - 1 - ry)
                        print("F -> C")
                    elif current_region == D:
                        next_facing = 3
                        next_x, next_y = bottom_edge(F, ry)
                        print("D -> F")
                    else:
                        raise Exception("Don't know what to do when moving right from region " + str(current_region))
                
            # DOWN
            elif facing == 1:
                next_x = x
                next_y = y + 1
                if next_y >= height or map[next_y][next_x] == " ":
                    current_region = region(x, y)
                    rx, ry = in_region(x, y)
                    if current_region == C:
                        next_facing = 2
                        next_x, next_y = right_edge(A, rx)
                        print("C -> A")
                    elif current_region == F:
                        next_facing = 2
                        next_x, next_y = right_edge(D, rx)
                        print("F -> D")
                    elif current_region == A:
                        next_x, next_y = top_edge(F, rx)
                        print("A -> F")
                    else:
                        raise Exception("Don't know what to do when moving down from region " + str(current_region))
                
            # LEFT
            elif facing == 2:
                next_x = x - 1
                next_y = y
                if next_x < 0 or map[next_y][next_x] == " ":
                    current_region = region(x, y)
                    rx, ry = in_region(x, y)
                    if current_region == B:
                        next_facing = 0
                        next_x, next_y = left_edge(E, BLOCKSIZE - 1 - ry)
                        print("B -> E")
                    elif current_region == D:
                        next_facing = 1
                        next_x, next_y = top_edge(B, ry)
                        print("D -> B")
                    elif current_region == A:
                        next_facing = 1
                        next_x, next_y = top_edge(E, ry)
                        print("A -> E")
                    elif current_region == E:
                        next_facing = 0
                        next_x, next_y = left_edge(B, BLOCKSIZE - 1 - ry)
                        print("E -> B")
                    else:
                        raise Exception("Don't know what to do when moving left from region " + str(current_region))
                
            # UP
            else:
                next_x = x
                next_y = y - 1
                if next_y < 0 or map[next_y][next_x] == " ":
                    current_region = region(x, y)
                    rx, ry = in_region(x, y)
                    if current_region == E:
                        next_facing = 0
                        next_x, next_y = left_edge(A, rx)
                        print("E -> A")
                    elif current_region == B:
                        next_facing = 0
                        next_x, next_y = left_edge(D, rx)
                        print("B -> D")
                    elif current_region == F:
                        next_x, next_y = bottom_edge(A, rx)
                        print("F -> A")
                    else:
                        raise Exception("Don't know what to do when moving up from region " + str(current_region))
                
            if map[next_y][next_x] == "#":
                break
                
            print(">V<^"[facing])
            
            facing = next_facing
            x = next_x
            y = next_y
            
print("Row:", y + 1, "Col:", x + 1, "Facing:", facing)
print("Result:", 1000 * y + 4 * x + facing + 1004)