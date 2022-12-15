x_y_distances = [
    (3844106, 3888618, 782759),
    (1380352, 1857923, 1512018),
    (272, 1998931, 11208),
    (2119959, 184595, 515371),
    (1675775, 2817868, 1126910),
    (2628344, 2174105, 913380),
    (2919046, 3736158, 610879),
    (16, 2009884, 20279),
    (2504789, 3988246, 773048),
    (2861842, 2428768, 425219),
    (3361207, 130612, 1702636),
    (831856, 591484, 1676930),
    (3125600, 1745424, 844805),
    (21581, 3243480, 1254650),
    (2757890, 3187285, 576126),
    (3849488, 2414083, 817668),
    (3862221, 757146, 990903),
    (3558604, 2961030, 803805),
    (3995832, 1706663, 1206407),
    (1082213, 3708082, 1620348),
    (135817, 1427041, 478176),
    (2467372, 697908, 1376097),
    (3448383, 3674287, 601367),
]

already_tried = []
try_these = [0]
overlaps = []

def run_test(TEST):

    row = 2000000 + TEST
    if row < 0 or row > 4000000: return
    print("testing y=", row)
    

    ranges = []

    def merge_range(r1, r2):
        a1, b1 = r1
        a2, b2 = r2
        
        if a1 > b1: return r2, None
        if a2 > b2: return r1, None
        
        overlap = a1 <= b2 and a2 <= b1
        
        if overlap:
            overlapAmount = 1 + (min(b1, b2) - max(a1, a2))
            overlaps.append((TEST, (overlapAmount + 1) // 2))
        
        if overlap: return (min(a1, a2), max(b1, b2)), None
        return r1, r2
        
    def compress_ranges():
        
        r1 = ranges.pop(0)
        for i in range(len(ranges)):
            r2 = ranges.pop(0)
            
            n1, n2 = merge_range(r1, r2)
            
            if n2: ranges.append(n2)
            else: ranges.append(n1); return True
        
        ranges.append(r1)
        return False

    for x, y, distance in x_y_distances:
        range_radius = distance - abs(y - row)
        
        new_range = (x - range_radius, x + range_radius)
        ranges.append(new_range)
        
    while len(ranges) > 1 and compress_ranges():
        pass
        
    if len(ranges) == 1:
        a,b = ranges[0]
        if a <= 0 and b >= 4000000: return
        
    print(ranges)
    input()
    
while try_these:
    for o in try_these:
        run_test(o)
    already_tried += try_these
    try_these = []
    for t, o in overlaps:
        if t + o not in already_tried:
            try_these.append(t + o)
        if t - o not in already_tried:
            try_these.append(t - o)
    overlaps = []
    input()
print("i tried them all")