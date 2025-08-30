from enum import Enum

class ResponseSignal(Enum):
    FILE_VALIDATED_SUCCESS ="File validated Successfully!"
    FILE_TYPE_NOT_SUPPORTED ="File type not supported!"
    FILE_SIZE_EXCEEDED ="Max file size excceeded!"
    FILE_UPLOAD_SUCCESS ="File uploaded Successfully!"
    FILE_UPLOAD_FAILED ="File upload Failed!"
    FILE_PROCESSING_FAILED ="File Processing Failed!"
    FILE_PROCESSING_SUCCESS ="File Processing Sucess!"
