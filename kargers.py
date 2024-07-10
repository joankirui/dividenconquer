import random
import copy

def read_graph(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = list(map(int, line.split()))
            graph[parts[0]] = parts[1:]
    return graph

def choose_random_edge(graph):
    v1 = random.choice(list(graph.keys()))
    v2 = random.choice(graph[v1])
    return v1, v2

def contract(graph, v1, v2):
    # Merge v2 into v1 and remove v2
    graph[v1].extend(graph[v2])
    for vertex in graph[v2]:
        graph[vertex].remove(v2)
        graph[vertex].append(v1)
    while v1 in graph[v1]:
        graph[v1].remove(v1)
    del graph[v2]

def karger_min_cut(graph):
    while len(graph) > 2:
        v1, v2 = choose_random_edge(graph)
        contract(graph, v1, v2)
    return len(list(graph.values())[0])

def repeated_karger_min_cut(file_path, iterations):
    original_graph = read_graph(file_path)
    min_cut = float('inf')
    for _ in range(iterations):
        graph = copy.deepcopy(original_graph)
        cut = karger_min_cut(graph)
        if cut < min_cut:
            min_cut = cut
    return min_cut

# File path to the adjacency list
file_path = './kargerMinCut.txt'

# Number of iterations to run the algorithm
iterations = 100

# Compute the minimum cut
min_cut = repeated_karger_min_cut(file_path, iterations)
print(f"The minimum cut is: {min_cut}")











# The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label, and the particular row (other entries except the first column) tells all the vertices that the vertex is adjacent to. So for example, the 
# 6
# 𝑡
# ℎ
# 6 
# th
#   row looks like : "6	155	56	52	120	......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc

# Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut.  (HINT: Note that you'll have to figure out an implementation of edge contractions.  Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction.  But you should also think about more efficient implementations.)   