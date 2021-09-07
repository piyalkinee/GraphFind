from fastapi import APIRouter

routes = APIRouter(prefix="/generator", tags=["Generator"])


@routes.post("/CreateDatabase", status_code=201)
async def create_database():
    
    

    return {"status": "ok"}
