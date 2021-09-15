from fastapi import APIRouter
from .services.dbgenerator import create_graph_for_sql, create_graph_for_neo4j
from .services.data import get_vertices, get_edges, delete_vertices, delete_edges
from modules.search.services.search import format_graph

routes = APIRouter(prefix="/Graph", tags=["Graph"])


@routes.get("/GetGraphData", status_code=201)
async def get_graph_data():

    data: dict = {}

    data["vertices"] = await get_vertices()
    data["edges"] = await get_edges()

    return data


@routes.post("/CreateGraph", status_code=201)
async def create_graph_with_data(vertex_count: int):

    await create_graph_for_sql(vertex_count)

    return {"status": "ok"}


@routes.delete("/DeleteGraphData", status_code=204)
async def delete_graph_data():

    await delete_vertices()
    await delete_edges()

    return {"status": "ok"}


@routes.post("/CreateGraphForNeo4j", status_code=201)
async def create_graph_for_neo4j_with_data():

    formated_graph: dict = format_graph(await get_edges())

    await create_graph_for_neo4j(formated_graph)

    return {"status": "ok"}
