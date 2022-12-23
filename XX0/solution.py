file = open("test_data.txt")
lines = file.readlines()
file.close()

data = []

for line in lines:
    data.append(int(line))

original = list(data)
l = len(data)

for number in original:
    current_position = data.index(number)
    left = data[:current_position]
    right = data[current_position + 1:]
    n = number % (l - 1)
    if n > 0:
        lr = right + left
        data = lr[:n] + [number] + lr[n:]
    else:
        lr = right + left
        data = lr[-n:] + [number] + lr[:-n]
    #print(number, data)

i = data.index(0)
k1 = data[(i + 1000) % l]
k2 = data[(i + 2000) % l]
k3 = data[(i + 3000) % l]

print(k1, k2, k3)
print(k1 + k2 + k3)
