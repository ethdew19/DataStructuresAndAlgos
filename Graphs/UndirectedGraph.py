graph = {
    'i': ['j','k'],
    'j' : ['i'],
    'k' : ['i','m','l'],
    'm' : ['k'],
    'l' : ['k'],
    'o' : ['n'],
    'n' : ['o']
}

#Is there a path between i and l

def HasPathUndirected(graph,src,target, visited = None):
    if visited == None:
        visited = set()
    if src in visited:
        return False
    visited.add(src)
    if src == target:
        return True
    for neighbor in graph[src]:
        if HasPathUndirected(graph,neighbor,target,visited):
            return True
    
    return False

print(HasPathUndirected(graph,'i','n'))



