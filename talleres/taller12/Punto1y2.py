from collections import deque

class graphAM:
    def __init__(self, nodes):
        self.graph = []
        for i in range(nodes):
            self.graph.append([])

def hayCaminoDFS(g, i, f):
    q = deque()
    q.append(i)
    while( len(q) != 0 ):
        n = q.pop()
        if (n == f):
            return True
        for hijito in g.getSuccessors(n):
            q.append(hijito)
    return False

def hayCaminoBFS(g, i, f):
    q = deque() 
    q.appendLeft(i)
    while( len(q) != 0 ):
        n = q.pop()
        if (n == f):
            return True
        for hijito in g.getSuccessors(n):
            q.appendLeft(hijito)
    return False
 

g = graphAM(5)
print(hayCaminoDFS(g,0,3))
    
# Creditos: Mauricio Toro