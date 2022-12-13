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

i = 0
total = 0

for p in pairs:
    i += 1
    split = p.split("\n")
    left = eval(split[0].strip())
    right = eval(split[1].strip())
    print(cmp(left, right, lambda: None))
    if cmp(left, right, lambda: None): total += i
    
print(total)