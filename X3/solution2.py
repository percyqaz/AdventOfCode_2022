file = open("test_data.txt")
pairs = file.read().split("\n\n")
file.close()

def cmp(left, right, otherwise):

    if left == [] and right == []: return otherwise()
    if left == []: return True
    if right == []: return False

    if isinstance(left[0], int) and isinstance(right[0], int):
        if left[0] < right[0]: return True
        elif left[0] > right[0]: return False
        else: return cmp (left[1:], right[1:], otherwise)
    if isinstance(left[0], int):
        return cmp ([left[0]], right[0], lambda: cmp (left[1:], right[1:], otherwise))
    if isinstance(right[0], int):
        return cmp (left[0], [right[0]], lambda: cmp (left[1:], right[1:], otherwise))
        
    return cmp (left[0], right[0], lambda: cmp (left[1:], right[1:], otherwise))

d1 = [[2]]
d2 = [[6]]
a = 1
b = 2

for p in pairs:
    split = p.split("\n")
    left = eval(split[0].strip())
    right = eval(split[1].strip())
    if cmp(left, d1, lambda: None): a += 1; b += 1
    elif cmp(left, d2, lambda: None): b += 1
    if cmp(right, d1, lambda: None): a += 1; b += 1
    elif cmp(right, d2, lambda: None): b += 1
    
print(a * b)