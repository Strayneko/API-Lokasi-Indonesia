from app.utils.api_dependencies import *
from app.models.Provinsi import Provinsi
from app.models.Kabupaten import Kabupaten
from app.models.Kecamatan import Kecamatan



class GetKecamatanResponseModel(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'code': status.HTTP_200_OK,
                'status': True,
                'message': strings.DATA_SUCCESS,
                'total': 1,
                'data': {
                    'extra_info': {
                        'provinsi': 'Jawa Tengah',
                        'kabupaten': 'Pemalang'
                    },
                'list': [{
                    'id': 3119,
                    'id_kabupaten': 13,
                    'nama': 'Taman',
                    }]
                },
            }
        }

class GetAllKecamatanResponseModel(BaseResponseModel):
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
                    'id': 3119,
                    'id_kabupaten': 214,
                    'nama': 'Taman',
                }]
                },
                'total_all_data': 1,
                'limit': 1,
                'next_offset': 0,
                'prev_offset': 0
            }
        }


async def get_kecamatan(id_kabupaten: int):
    with Session(db_engine) as session:

        kecamatan = session.query(Kecamatan.id, Kecamatan.nama, Kecamatan.id_kabupaten).filter(Kecamatan.id_kabupaten==id_kabupaten)
        if kecamatan.count() == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=strings.NO_DATA_FOUND
            )
        kabupaten = session.query(Kabupaten.id, Kabupaten.nama, Kabupaten.id_provinsi).filter(Kabupaten.id==id_kabupaten).first()
        provinsi   = session.query(Provinsi.nama).filter(Provinsi.id==kabupaten.id_provinsi).first()
    data = {
        'extra_info': {
            'provinsi': provinsi.nama,
            'kabupaten': kabupaten.nama
        },
        'list': kecamatan.all()
    }
    return GetKecamatanResponseModel(
        status_code=status.HTTP_200_OK,
        status=True,
        total=kecamatan.count(),
        data=data,
        message=strings.DATA_SUCCESS
    )
        
async def get_all_kecamatan(limit: int = 0, offset: int = 0):
    

    if limit == 0:
        limit = 100
    with Session(db_engine) as session:
        kecamatan = session.query(Kecamatan.id, Kecamatan.id_kabupaten, Kecamatan.nama)
        total_all_data = kecamatan.count()
        next_offset =  offset + limit if offset + limit < total_all_data else 0 
        prev_offset = offset - limit if offset - limit > 0 else 0
        
        # check offset and limit argument
        await check_limit_and_offset(kecamatan,limit=limit,offset=offset)
        kecamatan = kecamatan.limit(limit).offset(offset)


    data = {
        'list': kecamatan.all()
    }
    return GetAllKecamatanResponseModel(
        code=status.HTTP_200_OK,
        data=data,
        total=kecamatan.count(),
        limit=limit,
        message=strings.DATA_SUCCESS,
        next_offset=next_offset,
        prev_offset=prev_offset,
        total_all_data=total_all_data
    )