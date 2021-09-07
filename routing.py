from fastapi import APIRouter
from modules.generator import controller as generator_controller

routes = APIRouter()

routes.include_router(generator_controller.routes)