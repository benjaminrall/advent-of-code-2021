with open("input.txt", "r") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

nodes = {}
for line in lines:
    data = line.split("-")
    if data[0] in nodes:
        nodes[data[0]].append(data[1])
    else:
        nodes[data[0]] = [data[1]]
    if data[1] in nodes:
        nodes[data[1]].append(data[0])
    else:
        nodes[data[1]] = [data[0]]

def find_paths(nodes, currentNode = 'start', path = [], paths = [], usedTwo = False):
    if currentNode == 'end':
        paths.append(path + [currentNode])
        return paths
    for node in nodes[currentNode]:
        if (node.islower() and node not in path) or node.isupper():
            paths = find_paths(nodes, node, path + [currentNode], paths, usedTwo)
        elif not usedTwo and node != 'start':
            paths = find_paths(nodes, node, path + [currentNode], paths, True)
    return paths

paths = find_paths(nodes)
print(len(paths))