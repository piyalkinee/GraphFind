from fastapi import APIRouter
from modules.data.services.data import get_edges
from .services.search import format_graph, dfs_in_ram, bfs_in_ram

routes = APIRouter(prefix="/Search", tags=["Search"])


@routes.get("/DepthFirst", status_code=200)  # Поиск в глубину в памяти
async def depth_first_search(start: int, end: int):

    formated_graph: dict = format_graph(await get_edges())

    traversal_path = []
    traversal_path = dfs_in_ram(formated_graph, start, end, traversal_path)

    return traversal_path


@routes.get("/BreadthFirst", status_code=200)  # Поиск в ширину в памяти
async def breadth_first_search(start: int, end: int):

    formated_graph: dict = format_graph(await get_edges())

    traversal_path = []
    traversal_path = bfs_in_ram(formated_graph, start, end)

    return traversal_path
