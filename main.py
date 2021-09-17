from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from database.core import database_sql, neo4j_driver
from routing import routes

app = FastAPI(title="Graph Find")

app.include_router(routes)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
async def startup():
    await database_sql.connect()


@app.on_event("shutdown")
async def shutdown():
    await database_sql.disconnect()
    neo4j_driver.close()


@app.middleware("http")
async def middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    response = await call_next(request)
    return response
