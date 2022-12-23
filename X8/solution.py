file = open("test_data.txt")
data = file.readlines()
file.close()

points = set()

for line in data:
    split = line.strip().split(",")
    points.add((int(split[0]), int(split[1]), int(split[2])))

surface = 0

for x,y,z in points:
    if (x + 1, y, z) not in points:
        surface += 1
    if (x - 1, y, z) not in points:
        surface += 1
    if (x, y + 1, z) not in points:
        surface += 1
    if (x, y - 1, z) not in points:
        surface += 1
    if (x, y, z + 1) not in points:
        surface += 1
    if (x, y, z - 1) not in points:
        surface += 1

print(surface)
