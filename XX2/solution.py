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

def left_wrap(row):
    for x in range(width):
        if map[row][x] != " ":
            return x
            
def right_wrap(row):
    for x in range(width, 0, -1):
        if map[row][x - 1] != " ":
            return x - 1
            
def top_wrap(col):
    for y in range(height):
        if map[y][col] != " ":
            return y
            
def bottom_wrap(col):
    for y in range(height, 0, -1):
        if map[y - 1][col] != " ":
            return y - 1
            
x = left_wrap(0)
y = 0
facing = 0 # right, 1 = down, 2 = left, 3 = up
    
for move in path_parts:
    if move == "L":
        facing -= 1
        facing %= 4
    elif move == "R":
        facing += 1
        facing %= 4
    else:
        for i in range(move):
            if facing == 0:
                next_x = x + 1
                next_y = y
                if next_x >= width or map[next_y][next_x] == " ":
                    next_x = left_wrap(next_y)
                
            elif facing == 1:
                next_x = x
                next_y = y + 1
                if next_y >= height or map[next_y][next_x] == " ":
                    next_y = top_wrap(next_x)
                
            elif facing == 2:
                next_x = x - 1
                next_y = y
                if next_x < 0 or map[next_y][next_x] == " ":
                    next_x = right_wrap(next_y)
                
            else:
                next_x = x
                next_y = y - 1
                if next_y < 0 or map[next_y][next_x] == " ":
                    next_y = bottom_wrap(next_x)
                
            if map[next_y][next_x] == "#":
                break
            
            x = next_x
            y = next_y
            
print("Row:", y + 1, "Col:", x + 1, "Facing:", facing)
print("Result:", 1000 * y + 4 * x + facing + 1004)