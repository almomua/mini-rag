from fastapi import APIRouter , FastAPI , Depends
from helpers.config import get_settings, Settings
base_router = APIRouter(
    prefix="/api/v1",
    tags=["base"]
)

@base_router.get("/")
def welcome(app_settings : Settings = Depends(get_settings)):
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {"message": f"Welcome to the {app_name} API v{app_version}"}