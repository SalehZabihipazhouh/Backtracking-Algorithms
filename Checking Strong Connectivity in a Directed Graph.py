def create_graph(filename):    # This function create a graph from read the graph structures from text file and edges
    with open(filename,"r") as f:
        lines = f.readlines()
    vertex = int(lines[0].strip())
    graph = [[] for _ in range(vertex)]
    for line in lines[1:]:
        u, v, w = map(int,line.strip().split())
        if w == 1:
            graph[u].append(v)
    return graph

def reverse_graph(graph):      # This function create transpose graph from the original graph
    vertex = len(graph)
    re_graph = [[] for _ in range(vertex)]
    for u in range(vertex):
        for v in graph[u]:
            re_graph[v].append(u)
    return re_graph

def dfs(graph,node,visited):     # This function perform Depth-First search from given vertex(node) and mark all reachable vertex
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph,neighbor,visited)

def check_SCC(graph):     # This function check the graph is strongly connected or not
    vertex = len(graph)
    visited = [False] * vertex # Creates a list of bool type with the number of vertex
    dfs(graph,0,visited) # Perform DFS on original graph
    if not all(visited):  # If all nodes unvisited graph isn't strongly connected
        return False
    re_graph = reverse_graph(graph)  # If all node visited now we make transpose graph and assign in the re_graph
    visited = [False] * vertex   # Update the visited list with False again
    dfs(re_graph,0,visited)  # Perform DFS on transpose graph
    return all(visited) # If all node visited graph is strongly connected, otherwise it is not

if __name__ == "__main__":
    filename = str(input("Your file name :  ")) + ".txt" # Have to just enter the name of file without its format
    graph = create_graph(filename)
    print(check_SCC(graph))