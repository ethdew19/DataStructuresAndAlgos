#Adjacency list
#DFS - Depth first search


graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [] 
}

def depthFirstPrintIterative(graph,source):
    stack = [source]
    while len(stack) > 0:
        cur = stack.pop()
        print(cur)
        for neighbor in graph[cur]:
            stack.append(neighbor)

def DepthFirstSearchRecursive(graph,source):
    print(source)
    for neighbor in graph[source]:
        DepthFirstSearchRecursive(graph,neighbor)
        
def BreadthFirstSearch(graph,source):
    queue = [source]
    while len(queue) > 0:
        cur = queue.pop(0)
        print(cur)
        for neighbor in graph[cur]:
            queue.append(neighbor)
#depthFirstPrintIterative(graph,'a') #acebdf - valid dfs
#DepthFirstSearchRecursive(graph,'a')
#BreadthFirstSearch(graph,'a')