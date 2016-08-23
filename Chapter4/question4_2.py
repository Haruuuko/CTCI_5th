from Queue import deque

class Graph:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

def DFSFindRoute(node1, node2):
    if node1 == node2:
        return True
    node1.visited = True
    for node in node1.edges:
        if not node.visited:
            if DFSFindRoute(node, node2): return True
    return False

def BFSFindRoute(node1, node2):
    if node1 == node2: return True
    q = deque([node1])
    node1.visited = True
    while q:
        node = q.popleft()
        for n in node.edges:
            if n == node2:
                return True
            elif not n.visited:
                q.append(n)
                n.visited = True
    return False

n1 = Graph(1)
n2 = Graph(2)
n3 = Graph(3)
n4 = Graph(4)

n1.edges.append(n2)
n1.edges.append(n3)
#n3.edges.append(n4)

#print(DFSFindRoute(n1, n4))
print(BFSFindRoute(n1, n4))
