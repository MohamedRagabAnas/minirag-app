from helpers.config import get_settings, Settings

class BaseController:
    
    def __init__(self):
        self.app_setting =get_settings()
