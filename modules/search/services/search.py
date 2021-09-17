from database.core import database_sql, connect_neo4j, DB_NAME


def format_graph(edges):
    formated_graph: dict = {1: []}
    for e in edges:
        if int(e["to_id"]) not in formated_graph:
            formated_graph[int(e["to_id"])] = []
        formated_graph[int(e["from_id"])].append(int(e["to_id"]))

    return formated_graph


async def dfs_in_ram(formated_graph: dict, start, end):

    queue = []

    queue.append([start])
    while queue:

        path = queue.pop(-1)

        node = path[-1]

        if node == end:
            return path

        for adjacent in formated_graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


def bfs_in_ram(formated_graph, start, end):

    queue = []

    queue.append([start])
    while queue:

        path = queue.pop(0)

        node = path[-1]

        if node == end:
            return path

        for adjacent in formated_graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


async def dfs_in_mysql(start, end):
    query = f"""
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
    return [dict(d) for d in await database_sql.fetch_all(query)]


async def bfs_in_mysql(start, end):
    query = f"""
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
    return [dict(d) for d in await database_sql.fetch_all(query)]


async def dfs_in_neo4j(start, end):
    session = connect_neo4j()

    check_graph_list(session)

    query = """
    CALL gds.alpha.dfs.stream('[*DBNAME*]', {startNode:[*START*],targetNodes:[[*END*]]})
    YIELD path
    UNWIND [ n in nodes(path) | n.name ] AS names
    RETURN names
    """

    query = query.replace("[*DBNAME*]", str(DB_NAME+"_graph"))
    query = query.replace("[*START*]", str(start))
    query = query.replace("[*END*]", str(end))

    session.run(query)


async def bfs_in_neo4j(start, end):
    session = connect_neo4j()

    check_graph_list(session)

    query = """
    CALL gds.alpha.bfs.stream('[*DBNAME*]', {startNode:[*START*],targetNodes:[[*END*]]})
    YIELD path
    UNWIND [ n in nodes(path) | n.tag ] AS names
    RETURN names
    """

    query = query.replace("[*DBNAME*]", str(DB_NAME+"_graph"))
    query = query.replace("[*START*]", str(start))
    query = query.replace("[*END*]", str(end))

    session.run(query)


def check_graph_list(session):

    query = f"""
        CALL gds.graph.list
        """
    responce = session.run(query)

    if f"{DB_NAME}_graph" not in str(responce.single()):
        query = f"""
        CALL gds.graph.create('{DB_NAME}_graph', 'vertex', 'PARENT')
        """
        session.run(query)
