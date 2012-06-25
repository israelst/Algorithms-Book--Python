import heapq

def is_empty(l):
    return len(l) == 0

infinity = 999999
def prim(graph):
    cost = dict()
    prev = dict()
    for vertice in graph['vertices']:
        cost[vertice] = infinity
        prev[vertice] = None

    #Pick any initial node
    cost[graph['vertices'][0]] = 0

    priority_queue = [(c, v) for v, c in cost.iteritems()]
#    heapq.heapify(priority_queue) # priority queue, using cost-values as keys
    while not is_empty(priority_queue):
        priority_queue.sort()
        priority_queue.reverse()
        v = priority_queue.pop()[1]

#        v = heapq.heappop(priority_queue)[1]
        for edge in graph['edges'][v]:
            weight, z = edge
            if cost[z] > weight:
                cost[z] = weight
                prev[z] = (weight, v)
    return prev



graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': {
            'A': [
                (5, 'B'),
                (6, 'C'),
                (4, 'D'),
                ],
            'B': [
                (5, 'A'),
                (1, 'C'),
                (2, 'D'),
                ],
            'C': [
                (6, 'A'),
                (1, 'B'),
                (2, 'D'),
                (5, 'E'),
                (3, 'F'),
                ],
            'D': [
                (4, 'A'),
                (2, 'B'),
                (2, 'C'),
                (4, 'F'),
                ],
            'E': [
                (5, 'C'),
                (4, 'F'),
                ],
            'F': [
                (3, 'C'),
                (4, 'E'),
                (4, 'D'),
                ],
            }
        }
_graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
        'edges': {
            'A': [
                (5, 'B'),
                (6, 'C'),
                (4, 'D'),
                ],
            'B': [
                (1, 'C'),
                (2, 'D'),
                ],
            'C': [
                (2, 'D'),
                (5, 'E'),
                (3, 'F'),
                ],
            'D': [
                (4, 'F'),
                ],
            'E': [
                (4, 'F'),
                ],
            'F': [
                ],
            }
        }
minimum_spanning_tree = {
        'A': [
            (4, 'D'),
            ],
        'B': [
            (1, 'C'),
            (2, 'D'),
            ],
        'C': [
            (1, 'B'),
            (3, 'F'),
            ],
        'D': [
            (4, 'A'),
            (2, 'B'),
            ],
        'E': [
            (4, 'F'),
            ],
        'F': [
            (3, 'C'),
            (4, 'E'),
            ],
        }
assert prim(graph) == minimum_spanning_tree

