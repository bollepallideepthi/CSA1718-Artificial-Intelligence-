# Map Coloring using CSP (Backtracking)

colors = ["Red", "Green", "Blue"]

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

color_map = {}

def is_safe(region, color):
    for neighbor in graph[region]:
        if color_map.get(neighbor) == color:
            return False
    return True

def solve(regions, index):
    if index == len(regions):
        return True

    region = regions[index]

    for color in colors:
        if is_safe(region, color):
            color_map[region] = color
            if solve(regions, index + 1):
                return True
            color_map[region] = None
    return False

regions = list(graph.keys())

if solve(regions, 0):
    print("Map Coloring Solution:")
    for region in regions:
        print(region, "->", color_map[region])
else:
    print("No solution found.")