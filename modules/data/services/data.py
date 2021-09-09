from database.core import database, DB_NAME


async def get_vertices():
    querry = f"SELECT * FROM {DB_NAME}.vertices LIMIT 0, 10000"
    return [dict(d) for d in await database.fetch_all(querry)]


async def get_edges():
    querry = f"SELECT * FROM {DB_NAME}.edges LIMIT 0, 10000"
    return [dict(d) for d in await database.fetch_all(querry)]


async def delete_vertices():
    querry = f"TRUNCATE `{DB_NAME}`.`vertices`;"
    await database.execute(querry)

async def delete_edges():
    querry = f"TRUNCATE `{DB_NAME}`.`edges`;"
    await database.execute(querry)
