from database.core import database_sql, connect_neo4j, DB_NAME


async def get_vertices():
    query = f"SELECT * FROM {DB_NAME}.vertices LIMIT 0, 10000"
    return [dict(d) for d in await database_sql.fetch_all(query)]


async def get_edges():
    query = f"SELECT * FROM {DB_NAME}.edges LIMIT 0, 10000"
    return [dict(d) for d in await database_sql.fetch_all(query)]


async def delete_vertices():
    query = f"TRUNCATE `{DB_NAME}`.`vertices`;"
    await database_sql.execute(query)


async def delete_edges():
    query = f"TRUNCATE `{DB_NAME}`.`edges`;"
    await database_sql.execute(query)


async def delete_neo4j():
    session = connect_neo4j()

    query = f"""
        CALL gds.graph.list
        """
    responce = session.run(query)

    if f"{DB_NAME}_graph" in str(responce.single()):
        query = f"CALL gds.graph.drop('{DB_NAME}_graph') YIELD graphName;"
        session.run(query)

    query = f"MATCH (n:vertex) DETACH DELETE n"
    session.run(query)
