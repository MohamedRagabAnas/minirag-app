import imp
import re
from .BaseController import BaseController
from fastapi import UploadFile

class DataContrller(BaseController):

    def __init__(self):
        super().__init__()


    def validate_uploaded_file(self,file:UploadFile):

        if file.contentType not in self.app_settings.FILE_ALLOWED_TYPES:
            return False
        
        if file.size > self.app_settings.FILE_MAX_SIZE*1024:
            return False
        
    
        return True

            