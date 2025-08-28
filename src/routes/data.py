from asyncio.log import logger
from asyncore import write
import chunk
from sys import prefix
from helpers.config import get_settings, Settings
from fastapi import FastAPI, APIRouter,Depends,UploadFile, status
from fastapi.responses import JSONResponse
from controllers import DataController, ProjectController, ProcessController
import aiofiles
import os
from models import ResponseSignal
import logging
from .schemas.data  import ProcessRequest

logger= logging.getLogger("unicorn.error")

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"],
)
app=FastAPI()

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str , file: UploadFile,
                      app_settings:Settings =Depends(get_settings)):

                      
                      data_controller=DataController()
                      is_valid, msg = data_controller.validate_uploaded_file(file=file)
                      print(msg)
                      if not is_valid:
                          return JSONResponse(
                              status_code=status.HTTP_400_BAD_REQUEST,
                              content={
                                        "uploaded": is_valid,
                                        "signal": msg
                                       }
                              )
                      project_dir_path = ProjectController().get_project_path(project_id=project_id)
                      file_path,file_id = data_controller.generate_unique_filepath(
                          orignal_file_name=file.filename,
                          project_id=project_id
                      )
                      try:
                          async with aiofiles.open(file_path, "wb") as f:
                            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNCK_SIZE):
                                await f.write(chunk)
                      except Exception as e:
                         logger.error(f"error while uploading file: {e}") 
                         return JSONResponse(
                              status_code=status.HTTP_400_BAD_REQUEST,
                              content={
                                        "uploaded": is_valid,
                                        "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
                                       }
                              )

                        
                      return JSONResponse(
                          status_code=status.HTTP_200_OK,
                          content={
                              "uploaded": is_valid,
                              "msg": msg,
                              "fileId":str(file_id)
                              }
                              )
                        
                        
@data_router.post("/process/{project_id}")
async def process_endpoint(project_id:str, process_request:ProcessRequest):

    file_id= process_request.file_id

    process_controller = ProcessController(project_id)
    file_content=process_controller.get_file_content(file_id)

    return file_content



                        


