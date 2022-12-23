from math import ceil

file = open("test_data.txt")
lines = file.readlines()
file.close()

# type Blueprint = {
    #"ore": int,
    #"clay": int,
    #"obsidian": (int, int),
    #"geode": (int, int)
#}

blueprints = []

for line in lines[0:3]:
    split = line.split()
    blueprints.append({
            "ore": int(split[6]),
            "clay": int(split[12]),
            "obsidian": (int(split[18]), int(split[21])),
            "geode": (int(split[27]), int(split[30]))
        })

def robots_act(resources, robots, minutes):
    new_resources = resources.copy()
    for r in resources:
        new_resources[r] += robots[r] * minutes
    return new_resources

best_geode_count = 0

i = 1

def test_blueprint(blueprint):

    global best_geode_count

    robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
    resources = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
    minutes_left = 32
    best_geode_count = 0

    most_ore_needed = max(blueprint["ore"], blueprint["clay"], blueprint["obsidian"][0], blueprint["geode"][0])

    def consider_paths(blueprint, robots, resources, minutes_left):

        global best_geode_count
        global i

        projected_geodes = resources["geode"] + robots["geode"] * minutes_left
        if projected_geodes > best_geode_count:
            print(projected_geodes)
            best_geode_count = projected_geodes

        #print("time left:", minutes_left)
        #print("robots:", robots)
        #print("resources:", resources)
        #print("on pace for", projected_geodes, "geodes")
        #print()
        #input()

        # make geode robot
        if robots["obsidian"] > 0:

            ore_needed, obsidian_needed = blueprint["geode"]
            minutes_needed = max(
                    int(ceil((ore_needed - resources["ore"]) / robots["ore"])),
                    int(ceil((obsidian_needed - resources["obsidian"]) / robots["obsidian"]))
                )
            if minutes_needed < 0: minutes_needed = 0

            if minutes_needed < minutes_left - 1:
                # wait for robots to make resources + minute to craft
                new_resources = robots_act(resources, robots, minutes_needed + 1)
                # spend a minute crafting the robot
                new_resources["ore"] -= ore_needed
                new_resources["obsidian"] -= obsidian_needed
                new_minutes = minutes_left - minutes_needed - 1
                new_robots = robots.copy()
                new_robots["geode"] += 1

                consider_paths(blueprint, new_robots, new_resources, new_minutes)

        # make obsidian robot
        if robots["clay"] > 0 and robots["obsidian"] < blueprint["geode"][1]:

            ore_needed, clay_needed = blueprint["obsidian"]
            minutes_needed = max(
                    int(ceil((ore_needed - resources["ore"]) / robots["ore"])),
                    int(ceil((clay_needed - resources["clay"]) / robots["clay"]))
                )
            if minutes_needed < 0: minutes_needed = 0

            if minutes_needed < minutes_left - 1:
                # wait for robots to make resources + minute to craft
                new_resources = robots_act(resources, robots, minutes_needed + 1)
                # spend a minute crafting the robot
                new_resources["ore"] -= ore_needed
                new_resources["clay"] -= clay_needed
                new_minutes = minutes_left - minutes_needed - 1
                new_robots = robots.copy()
                new_robots["obsidian"] += 1

                consider_paths(blueprint, new_robots, new_resources, new_minutes)

        # make clay robot
        if robots["clay"] < blueprint["obsidian"][1]:

            ore_needed = blueprint["clay"]
            minutes_needed = int(ceil((ore_needed - resources["ore"]) / robots["ore"]))
            if minutes_needed < 0: minutes_needed = 0

            if minutes_needed < minutes_left - 1:
                # wait for robots to make resources + minute to craft
                new_resources = robots_act(resources, robots, minutes_needed + 1)
                # spend a minute crafting the robot
                new_resources["ore"] -= blueprint["clay"]
                new_minutes = minutes_left - minutes_needed - 1
                new_robots = robots.copy()
                new_robots["clay"] += 1

                consider_paths(blueprint, new_robots, new_resources, new_minutes)

        # make ore robot
        if robots["ore"] < most_ore_needed:

            ore_needed = blueprint["ore"]
            minutes_needed = int(ceil((ore_needed - resources["ore"]) / robots["ore"]))
            if minutes_needed < 0: minutes_needed = 0

            if minutes_needed < minutes_left - 1:
                # wait for robots to make resources + minute to craft
                new_resources = robots_act(resources, robots, minutes_needed + 1)
                # spend a minute crafting the robot
                new_resources["ore"] -= blueprint["ore"]
                new_minutes = minutes_left - minutes_needed - 1
                new_robots = robots.copy()
                new_robots["ore"] += 1

                consider_paths(blueprint, new_robots, new_resources, new_minutes)

    consider_paths(blueprint, robots, resources, minutes_left)
    return best_geode_count

total = 1

for blueprint in blueprints:
    print(i, "..")
    total *= test_blueprint(blueprint)
    i += 1

print(total)
