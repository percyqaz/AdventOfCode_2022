file = open("test_data.txt")
data = file.readlines()
file.close()

points = set()

air = set()

for line in data:
    split = line.strip().split(",")
    points.add((int(split[0]), int(split[1]), int(split[2])))

surface = 0

check_next = [(-1, -1, -1)]

def pt(x, y, z):
    if x < -1 or x > 25 or y < -1 or y > 25 or z < -1 or z > 25:
        return
    if (x, y, z) not in points and (x, y, z) not in air:
        air.add((x, y, z))
        check_next.append((x, y, z))

print("mapping out air...")

while check_next:
    x, y, z = check_next.pop(0)
    pt(x + 1, y, z)
    pt(x - 1, y, z)
    pt(x, y + 1, z)
    pt(x, y - 1, z)
    pt(x, y, z + 1)
    pt(x, y, z - 1)

print("calculating surface...")

for x, y, z in points:
    if (x + 1, y, z) in air:
        surface += 1
    if (x - 1, y, z) in air:
        surface += 1
    if (x, y + 1, z) in air:
        surface += 1
    if (x, y - 1, z) in air:
        surface += 1
    if (x, y, z + 1) in air:
        surface += 1
    if (x, y, z - 1) in air:
        surface += 1

print(surface)
