from fastapi import APIRouter
from .services.dbgenerator import create_graph_for_sql
from .services.data import get_vertices, get_edges

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
