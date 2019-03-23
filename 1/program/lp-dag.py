import collections

# Read file
def ReadFile(filename):
    numV = 0
    numE = 0
    listEdges = []
    # read file and remove \n
    with open(filename) as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
    # read file line by line
    #     first line: number of vertices
    #     second line: number of edges
    #     other lines: connected vertices each connection is an edge
    for i, line in enumerate(lines):
        if(i == 0):
            numV = int(line)
        elif(i == 1):
            numE = int(line)
        else:
            listEdges.append(line.split())
    # turn list into adjList
    adjListEdges = collections.defaultdict(list)
    for (x, y) in listEdges:
        adjListEdges[x].append(y)
    return numV, numE, adjListEdges

# DFS algorithm
def DFS(adjListEdges, vertex, visited=None, path=None):
    if visited is None:
        visited = []
    if path is None:
        path = [vertex]
    visited.append(vertex)
    paths = []
    for neighbor in adjListEdges[vertex]:
        if neighbor not in visited:
            neighbor_path = path + [neighbor]
            paths.append(tuple(neighbor_path))
            paths.extend(DFS(adjListEdges, neighbor, visited[:], neighbor_path))
    return paths

# Get the longest paths
def GetMax(adjListEdges, numV):
    all_paths_global = []
    max_len_global = 0
    max_paths_global = 0
    for i in range(1,numV+1):
        all_paths = DFS(adjListEdges, str(i))
        all_paths_global.append(all_paths)
        if(all_paths !=  []):
            max_len = 0
            for path in all_paths:
                if(len(path) > max_len):
                    max_paths = path
                    max_len = len(path)
            if(max_len > max_len_global):
                max_len_global = max_len
                max_paths_global = max_paths
    return all_paths_global, max_len_global, max_paths_global

# Display the longest paths
def DisplayAll(all_paths_global):
    print("All Paths:")
    for i, all_paths in enumerate(all_paths_global):
        print(str(i)+':', all_paths)

# Display the length of the longest path with the path of one of the longest paths
def DisplayMax(max_len, max_paths):
    print("Length of longest path: "+str(max_len-1))
    print("Path: ", end='')
    for i, path in enumerate(max_paths):
        if(i == len(max_paths)-1):
            print(path, end='\n')
        else:
            print(str(path)+'-', end='')

if __name__ == "__main__":
    numV, numE, adjListEdges = ReadFile('graph.txt')
    all_paths, max_len, max_paths = GetMax(adjListEdges, numV)
    DisplayMax(max_len, max_paths)
