from app.utils.api_dependencies import *

from app.models.Provinsi import Provinsi
from app.models.Kabupaten import Kabupaten


class GetKabupatenResponseModel(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'code': status.HTTP_200_OK,
                'status': True,
                'message': strings.DATA_SUCCESS,
                'total': 1,
                'data': {
                    'extra_data': {
                        'provinsi': 'Jawa Tengah'
                    },
                    'list':[{
                    'id': 214,
                    'id_provinsi': 13,
                    'nama': 'Pemalang',
                }]
                },
            }
        }

class GetAllKabupatenResponseModel(BaseResponseModel):
    total_all_data: int = 0
    limit: int = 0
    next_offset: int = 0
    prev_offset: int = 0
    class Config:
        schema_extra = {
            'example': {
                'code': status.HTTP_200_OK,
                'status': True,
                'message': strings.DATA_SUCCESS,
                'total': 1,
                'data': {
                    'list':[{
                    'id': 214,
                    'id_provinsi': 13,
                    'nama': 'Pemalang',
                }]
                },
                'total_all_data': 1,
                'limit': 1,
                'next_offset': 0,
                'prev_offset': 0
            }
        }



async def get_kabupaten(id_provinsi: int):
    with Session(db_engine) as session:
        kabupaten = session.query(Kabupaten.id, Kabupaten.id_provinsi, Kabupaten.nama).filter(Kabupaten.id_provinsi==id_provinsi)
        if kabupaten.count() == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=strings.NO_DATA_FOUND
            )
        provinsi  = session.query(Provinsi).filter(Provinsi.id==id_provinsi).first()
       



    data = {
        'extra_info': {
            'provinsi': provinsi.nama,
        },
        'list': kabupaten.all()
    }
    return GetKabupatenResponseModel(
        code=status.HTTP_200_OK,
        status=True,
        data=data,
        total=kabupaten.count(),
        message=strings.DATA_SUCCESS
            
    )

async def get_all_kabupaten(limit: int = 0, offset: int = 0):
    

    if limit == 0:
        limit = 100
    with Session(db_engine) as session:
        kabupaten = session.query(Kabupaten.id, Kabupaten.id_provinsi, Kabupaten.nama)
        total_all_data = kabupaten.count()
        next_offset =  offset + limit if offset + limit < total_all_data else 0 
        prev_offset = offset - limit if offset - limit > 0 else 0
        
        # check offset and limit argument
        await check_limit_and_offset(kabupaten,limit=limit,offset=offset)
        kabupaten = kabupaten.limit(limit).offset(offset)


    data = {
        'list': kabupaten.all()
    }
    return GetAllKabupatenResponseModel(
        code=status.HTTP_200_OK,
        data=data,
        total=kabupaten.count(),
        limit=limit,
        message=strings.DATA_SUCCESS,
        next_offset=next_offset,
        prev_offset=prev_offset,
        total_all_data=total_all_data
    )