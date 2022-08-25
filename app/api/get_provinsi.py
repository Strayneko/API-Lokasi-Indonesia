from app.utils.api_dependencies import *
from app.api_model import BaseResponseModel
from app.models.Provinsi import Provinsi


class GetProvinsiResponseModel(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'code': status.HTTP_200_OK,
                'status': True,
                'message': strings.DATA_SUCCESS,
                'total':1,
                'data': {
                  'list': [{
                    'nama': 'Jawa Tengah',
                    'id': 13,
                  }]
                },
            }
        }

async def get_provinsi():

    with Session(db_engine) as session:
        province = session.query(Provinsi)

        if province.count() == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=strings.NO_DATA_FOUND
            )

        return GetProvinsiResponseModel(
            total = province.count(),
            data = {'list': province.all()},
            message=strings.DATA_SUCCESS
        )

