
def format_graph(edges):
    formated_graph: dict = {1: []}
    for e in edges:
        if int(e["to_id"]) not in formated_graph:
            formated_graph[int(e["to_id"])] = []
        formated_graph[int(e["from_id"])].append(int(e["to_id"]))

    return formated_graph


def dfs_in_ram(formated_graph, start, end, path, visited=set()):
    path.append(start)
    visited.add(start)
    if start == end:
        return path
    for neighbour in formated_graph[start]:
        if neighbour not in visited:
            result = dfs_in_ram(formated_graph, neighbour, end, path, visited)
            if result is not None:
                return result
            path.pop()
    return None


def bfs_in_ram(formated_graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a 
        # new path and push it into the queue
        for adjacent in formated_graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)