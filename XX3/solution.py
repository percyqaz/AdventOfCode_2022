file = open("test_data.txt")
data = file.readlines()
file.close()

elves = {}

y = 0
for line in data:
    for x in range(len(line)):
        if line[x] == "#":
            elves[(x, y)] = None
    y += 1
    
proposals = {}

def should_move(elf_pos):
    x, y = elf_pos
    if (x - 1, y + 1) in elves: return True
    if (x,     y + 1) in elves: return True
    if (x + 1, y + 1) in elves: return True
    if (x + 1, y    ) in elves: return True
    if (x + 1, y - 1) in elves: return True
    if (x,     y - 1) in elves: return True
    if (x - 1, y - 1) in elves: return True
    if (x - 1, y    ) in elves: return True
    return False

def propose(elf_pos, x, y):
    elves[elf_pos] = (x, y)
    try: proposals[(x, y)] += 1 
    except KeyError: proposals[(x, y)] = 1
    
def north(elf_pos):
    x, y = elf_pos
    if (x - 1, y - 1) in elves: return False
    if (x,     y - 1) in elves: return False
    if (x + 1, y - 1) in elves: return False
    propose(elf_pos, x, y - 1)
    return True
    
def south(elf_pos):
    x, y = elf_pos
    if (x - 1, y + 1) in elves: return False
    if (x,     y + 1) in elves: return False
    if (x + 1, y + 1) in elves: return False
    propose(elf_pos, x, y + 1)
    return True
    
def west(elf_pos):
    x, y = elf_pos
    if (x - 1, y - 1) in elves: return False
    if (x - 1, y    ) in elves: return False
    if (x - 1, y + 1) in elves: return False
    propose(elf_pos, x - 1, y)
    return True
    
def east(elf_pos):
    x, y = elf_pos
    if (x + 1, y - 1) in elves: return False
    if (x + 1, y    ) in elves: return False
    if (x + 1, y + 1) in elves: return False
    propose(elf_pos, x + 1, y)
    return True

def display():

    l = 9999999
    r = -9999999
    t = 9999999
    b = -9999999
        
    for x, y in elves:
        if x < l: l = x
        if x > r: r = x
        if y > b: b = y
        if y < t: t = y
        
    c = 0
    for y in range(t, b + 1):
        line = ""
        for x in range(l, r + 1):
            if (x, y) not in elves:
                c += 1
                line += "."
            else:
                line += "#"
        print(line)
    print("----")
    print(c)

rotation = [north, south, west, east]

for i in range(10):

    # proposal phase

    for elf in list(elves):
        if should_move(elf):
            for dir in rotation:
                if dir(elf): break
            
    rotation.append(rotation.pop(0))
    
    # move phase
    
    new_elves = {}
           
    for elf in list(elves):
        proposal = elves[elf]
        if proposal and proposals[proposal] <= 1:
            new_elves[proposal] = None
        else:
            new_elves[elf] = None
    elves = new_elves
    proposals = {}
            
    # display
            
    display()
    