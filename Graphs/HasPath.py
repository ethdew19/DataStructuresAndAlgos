graph = {
    'f': ['g','i'],
    'h': [],
    'g': ['h'],
    'i': ['g','k'],
    'j': ['i'],
    'k': []
}

def hasPathDFSRec(graph,src,target):
    if src == target:
        return True
    for j in graph[src]:
        if hasPathDFSRec(graph,j,target):
            return True
    return False
def hasPathBFS(graph,src,target):
    q = [src]
    while len(q) > 0:
        cur = q.pop(0)
        if cur == target:
            return True
        for neighbor in graph[cur]:
            q.append(neighbor)
    return False   

#print(hasPathDFSRec(graph,'f','k'))
print(hasPathBFS(graph,'f','k')) 

