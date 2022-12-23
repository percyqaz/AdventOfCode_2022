file = open("test_data.txt")
lines = file.readlines()
file.close()

data = []

id = 0
for line in lines:
    if line.strip() == "0":
        print("zero")
        data.append((0, -1))
    else:
        data.append((int(line) * 811589153, id))
        id += 1

original = list(data)
l = len(data)

for i in range(10):
    print("mix", i + 1, "..")
    for number in original:
        current_position = data.index(number)
        left = data[:current_position]
        right = data[current_position + 1:]
        n = number[0] % (l - 1)
        if n > 0:
            lr = right + left
            data = lr[:n] + [number] + lr[n:]
        else:
            lr = right + left
            data = lr[-n:] + [number] + lr[:-n]
        #print(number, data)

i = data.index((0, -1))
k1 = data[(i + 1000) % l][0]
k2 = data[(i + 2000) % l][0]
k3 = data[(i + 3000) % l][0]

print(k1, k2, k3)
print(k1 + k2 + k3)
