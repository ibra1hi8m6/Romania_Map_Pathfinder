graph = {
    'Arad': [('Sibiu',140), ('Zerind',75), ('Timisoara',118)], 
    'Zerind': [('Arad',75), ('Oradea',71)],
    'Oradea': [('Zerind',71), ('Sibiu',151)],
    'Sibiu': [('Arad',140), ('Oradea',151), ('Fagaras',99), ('Rimnicu Vilcea',80)],
    'Timisoara': [('Arad',118), ('Lugoj',111)],
    'Lugoj': [('Timisoara',111), ('Mehadia',70)],
    'Mehadia': [('Lugoj',70), ('Drobeta',75)],
    'Drobeta': [('Mehadia',75), ('Craiova',120)],
    'Craiova': [('Drobeta',120), ('Rimnicu Vilcea',146), ('Pitesti',138)],
    'Rimnicu Vilcea': [('Sibiu',80), ('Craiova',146), ('Pitesti',97)],
    'Fagaras': [('Sibiu',99), ('Bucharest',211)],
    'Pitesti': [('Rimnicu Vilcea',97), ('Craiova',138), ('Bucharest',101)],
    'Bucharest': [('Fagaras',211), ('Pitesti',101), ('Giurgiu',90), ('Urziceni',85)],
    'Giurgiu': [('Bucharest',90)],
    'Urziceni': [('Bucharest',85), ('Vaslui',142), ('Hirsova',98)],
    'Hirsova': [('Urziceni',98), ('Eforie',86)],
    'Eforie': [('Hirsova',86)],
    'Vaslui': [('Iasi',92), ('Urziceni',142)],
    'Iasi': [('Vaslui',92), ('Neamt',87)],
    'Neamt': [('Iasi',87)]
}

def DFS(graph,start,goal):
    visited=[]
    stack=[[(start,0)]]
    while stack:
        path=stack.pop()
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes=graph.get(node,[])
            for(node2,cost) in adjacent_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                stack.append(new_path)
    return None

def DFSL(start, limit, graph, goal):
    visited = []
    stack = [[(start, 0)]]
    while stack:
        path = stack.pop()
        node = path[-1][0]
        depth = len(path) - 1
        if node == goal:
            return path
        if depth < limit:
            if node in visited:
                continue
            visited.append(node)
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                stack.append(new_path)
    return None

def iterativeDFSL(graph, start, goal):
    if goal not in graph or start not in graph:
        return None
    result = None
    limit = 0
    while not result:
        result = DFSL(start, limit, graph, goal)
        limit += 1
    return result

H_table = {
    
    'Arad': 366, 
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara':329 ,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Fagaras': 178,
    'Pitesti': 98,
    'Bucharest': 0,
    'Giurgiu': 77,
    'Urziceni': 80,
    'Hirsova': 151,
    'Eforie': 161,
    'Vaslui': 199,
    'Iasi': 226,
    'Neamt': 234
}

def path_f_cost(path):
    g_cost=0
    for (node,cost) in path:
        g_cost+=cost
    last_node=path[-1][0]
    h_cost=H_table[last_node]
    f_cost=h_cost+g_cost
    return f_cost,last_node

def A_star(graph,start,goal):
    visited=[]
    queue=[[(start,0)]]
    while queue:
        queue.sort(key=path_f_cost)
        path=queue.pop(0)
        node=path[-1][0]
        if node not in visited:
            visited.append(node)
            if node == goal:
                return path
            else:
                adjacent_nodes=graph.get(node,[])
                for(node2,cost) in adjacent_nodes:
                    new_path=path.copy()
                    new_path.append((node2,cost))
                    queue.append(new_path)