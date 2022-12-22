file = open("test_data.txt")
lines = file.readlines()
file.close()

valves = {}

for line in lines:
    split = line.split()

    name = split[1]
    rate = int(split[4][5:-1])
    tunnels = " ".join(split[9:]).split(", ")

    valves[name] = { "rate": rate, "tunnels": tunnels }

current = "AA"

print("identifying notable nodes...")

important_nodes = [current]
priorities = []
for node in valves:
    if valves[node]["rate"] > 0:
        important_nodes.append(node)
    priorities.append((valves[node]["rate"], node))

def dijkstra(source):
    distances = {}
    visited = {}
    for node in valves:
        visited[node] = False
        distances[node] = 99999
    distances[source] = 0

    explore_next = [source]

    def explore(current):
        for node in valves[current]["tunnels"]:
            if not visited[node]:
                new_dist = distances[current] + 1
                if new_dist < distances[node]:
                    distances[node] = new_dist
                explore_next.append(node)
        visited[current] = True

    while explore_next:
        explore(explore_next.pop(0))

    return distances

smaller_graph = {}

print("generating reduced graph...")

for node in important_nodes:
    smaller_graph[node] = { "rate": valves[node]["rate"], "paths": dijkstra(node) }

print("exploring smaller graph...")

best_score = 0

def paths(location, minutes_left, score, graph):
    global best_score

    # open this valve
    score = graph[location]["rate"] * minutes_left + score
    minutes_left = minutes_left - 1
    graph = graph.copy()
    distances = graph[location]["paths"]
    del graph[location]

    # try to explore more
    for node in graph:
        if distances[node] < minutes_left:
            paths(node, minutes_left - distances[node], score, graph)

    # update best score
    if score > best_score:
        best_score = score

paths(current, 30, 0, smaller_graph)
print("best score:", best_score)
