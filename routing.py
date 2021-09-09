from fastapi import APIRouter
from modules.main import controller as main_controller
from modules.data import controller as data_controller
from modules.search import controller as search_controller

routes = APIRouter()

routes.include_router(main_controller.routes)
routes.include_router(data_controller.routes)
routes.include_router(search_controller.routes)
