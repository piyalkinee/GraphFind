from database.core import database, DB_NAME


def format_graph(edges):
    formated_graph: dict = {1: []}
    for e in edges:
        if int(e["to_id"]) not in formated_graph:
            formated_graph[int(e["to_id"])] = []
        formated_graph[int(e["from_id"])].append(int(e["to_id"]))

    return formated_graph


async def dfs_in_ram(formated_graph, start, end, path, visited=set()):
    path.append(start)
    visited.add(start)
    if start == end:
        return path
    for neighbour in formated_graph[start]:
        if neighbour not in visited:
            result = await dfs_in_ram(formated_graph, neighbour, end, path, visited)
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


async def dfs_in_mysql(start, end):
    querry = f"""
    WITH RECURSIVE pathfind AS
    (
    SELECT from_id, CAST(from_id AS CHAR(500)) AS path
    FROM {DB_NAME}.edges
    WHERE from_id='{start}'
    UNION
    SELECT t.from_id, CONCAT(d.path, ',', t.from_id)
    FROM pathfind d, {DB_NAME}.edges t
    WHERE t.to_id=d.from_id
    )
    SELECT * FROM pathfind ORDER BY path;
    """
    return [dict(d) for d in await database.fetch_all(querry)]


async def bfs_in_mysql(start, end):
    querry = f"""
    WITH RECURSIVE pathfind AS
    (
    SELECT from_id, 1 as level
    FROM {DB_NAME}.edges
    WHERE from_id='{start}'
    UNION
    SELECT t.from_id, d.level+1
    FROM pathfind d, {DB_NAME}.edges t
    WHERE t.to_id=d.from_id
    )
    SELECT * FROM pathfind ORDER BY level;
    """
    return [dict(d) for d in await database.fetch_all(querry)]
