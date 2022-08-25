from fastapi import Request
from app.utils.api_dependencies import *
from app.api_model import BaseResponseModel
from app.models.Provinsi import Provinsi


class RootResponseModel(BaseResponseModel):

    class Config():

        schema_extra = {
            'example': {
                'code': status.HTTP_200_OK,
                'status': True,
                'message': strings.ROOT_MESSAGE,
                'total':1,
                'data': {
                'creator': {
                        'name': strings.CREATOR_NAME,
                        'github': strings.CREATOR_GITHUB,
                        'site': strings.CREATOR_SITE,
                        'email': strings.CREATOR_MAIL,
                        },
                'project_repository': strings.PROJECT_REPOSITORY
                
                },
            }
        }

async def root(request: Request):
    data = {
        'creator': {
            'name': strings.CREATOR_NAME,
            'github': strings.CREATOR_GITHUB,
            'site': strings.CREATOR_SITE,
            'email': strings.CREATOR_MAIL,
        },
        'project_repository': strings.PROJECT_REPOSITORY,
        'docs': request.base_url._url + 'docs',
        'api_url': request.base_url._url + 'api'
    }
    return RootResponseModel(message=strings.ROOT_MESSAGE, data=data, total=1);