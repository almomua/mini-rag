from fastapi import APIRouter , FastAPI , Depends, UploadFile, File , status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers.DataController import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str , file:UploadFile , app_settings:Settings = Depends(get_settings)):
    is_valid , result_signal = DataController().validate_uploaded_file(file)
    if not is_valid:
        return JSONResponse(content={"signal": result_signal}, status_code=status.HTTP_400_BAD_REQUEST)
    return JSONResponse(content={"signal": result_signal}, status_code=status.HTTP_200_OK)