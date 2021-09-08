from database.core import database, DB_NAME


async def get_vertices():
    querry = f"SELECT * FROM graphfinddb.vertices LIMIT 0, 10000"
    return [dict(d) for d in await database.fetch_all(querry)]


async def get_edges():
    querry = f"SELECT * FROM graphfinddb.edges LIMIT 0, 10000"
    return [dict(d) for d in await database.fetch_all(querry)]
