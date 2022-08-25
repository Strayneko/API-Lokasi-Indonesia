from typing import Union
from pydantic import BaseModel
from fastapi.responses import JSONResponse


class BaseResponseModel(BaseModel):
    code: int = 200
    status: bool = True
    message: str = 'success'
    total: int = 0
    data: Union[dict, list] = {}
    
    class Config:
        schema_extra = {
            'example': {
                'code': 200,
                'status': True,
                'message': 'success',
                'total': 0,
                'data': None,
            }
        }


async def http_exception_handler(request, exc):
    response = {
        'code': exc.status_code,
        'message': exc.detail,
    }
    return JSONResponse(response)

async def validation_exception_handler(request, exc):
    response = {
        'message' : exc.errors()[0]['msg'],
        'type'    : exc.errors()[0]['type']
    }
    return JSONResponse(response)