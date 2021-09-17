from fastapi import APIRouter
from modules.data.services.data import get_edges
from .services.search import format_graph, dfs_in_ram, bfs_in_ram, dfs_in_mysql, bfs_in_mysql, dfs_in_neo4j, bfs_in_neo4j
import time

routes = APIRouter(prefix="/Search", tags=["Search"])


@routes.get("/Ram/DepthFirst", status_code=200)  # Поиск в глубину в памяти
async def depth_first_search_ram(start: int, end: int):

    formated_graph: dict = format_graph(await get_edges())

    traversal_path = []

    time_start = time.time()

    traversal_path = await dfs_in_ram(formated_graph, start, end)

    time_resolt = time.time() - time_start

    return {"time": time_resolt, "path": traversal_path}


@routes.get("/Ram/BreadthFirst", status_code=200)  # Поиск в ширину в памяти
async def breadth_first_search_ram(start: int, end: int):

    formated_graph: dict = format_graph(await get_edges())

    traversal_path = []

    time_start = time.time()

    traversal_path = bfs_in_ram(formated_graph, start, end)

    time_resolt = time.time() - time_start

    return {"time": time_resolt, "path": traversal_path}


@routes.get("/MySQL/DepthFirst", status_code=200)  # Поиск в глубину в mysql
async def depth_first_search_mysql(start: int, end: int):

    traversal_path = []

    time_start = time.time()

    traversal_path = await dfs_in_mysql(start, end)

    time_resolt = time.time() - time_start

    return {"time": time_resolt, "path": traversal_path}


@routes.get("/MySQL/BreadthFirst", status_code=200)  # Поиск в глубину в mysql
async def depth_first_search_mysql(start: int, end: int):

    traversal_path = []

    time_start = time.time()

    traversal_path = await bfs_in_mysql(start, end)

    time_resolt = time.time() - time_start

    return {"time": time_resolt, "path": traversal_path}


@routes.get("/Neo4j/DepthFirst", status_code=200)  # Поиск в глубину в neo4j
async def depth_first_search_neo4j(start: int, end: int):

    traversal_path = []

    time_start = time.time()

    traversal_path = await dfs_in_neo4j(start, end)

    time_resolt = time.time() - time_start

    return {"time": time_resolt, "path": traversal_path}


@routes.get("/Neo4j/BreadthFirst", status_code=200)  # Поиск в глубину в neo4j
async def depth_first_search_neo4j(start: int, end: int):

    traversal_path = []

    time_start = time.time()

    traversal_path = await bfs_in_neo4j(start, end)

    time_resolt = time.time() - time_start

    return {"time": time_resolt, "path": traversal_path}
