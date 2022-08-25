from app.utils.api_dependencies import *
from app.models.Provinsi import Provinsi
from app.models.Kabupaten import Kabupaten
from app.models.Kecamatan import Kecamatan
from app.models.Kelurahan import Kelurahan


class GetKelurahanResponseModel(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'code': status.HTTP_200_OK,
                'status': True,
                'message': 'success',
                'total': 1,
                'data': {
                    'extra_info': {
                        'provinsi': 'Jawa Tengah',
                        'kabupaten': 'Pemalang',
                        'kecamatan': 'Taman'
                    },
                'list': [{
                    'id': 39155,
                    'id_kecamatan': 3119,
                    'nama': 'Wanarejan Selatan',
                }]
                },
            }
        }


class GetAllKelurahanResponseModel(BaseResponseModel):
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


async def get_kelurahan(id_kecamatan: int):
    with Session(db_engine) as session:
        kelurahan = session.query(Kelurahan.id, Kelurahan.id_kecamatan, Kelurahan.nama
        ).filter(Kelurahan.id_kecamatan==id_kecamatan)
        if kelurahan.count() == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=strings.NO_DATA_FOUND
            )
        kecamatan = session.query(Kecamatan.nama, Kecamatan.id_kabupaten).filter(Kecamatan.id==id_kecamatan).first()
        kabupaten = session.query(Kabupaten.nama, Kabupaten.id_provinsi).filter(Kabupaten.id==kecamatan.id_kabupaten).first()
        provinsi  = session.query(Provinsi.nama).filter(Provinsi.id==kabupaten.id_provinsi).first()

    
    data = {
        'extra_info': {
            'provinsi': provinsi.nama,
            'kabupaten': kabupaten.nama,
            'kecamatan': kecamatan.nama

        },
        'list': kelurahan.all()
    }
    return GetKelurahanResponseModel(
        status_code=status.HTTP_200_OK,
        total=kelurahan.count(),
        message=strings.DATA_SUCCESS,
        data=data
    )

async def get_all_kelurahan(limit: int = 0, offset: int = 0):
    

    if limit == 0:
        limit = 100
    with Session(db_engine) as session:
        kelurahan = session.query(Kelurahan.id, Kelurahan.id_kecamatan, Kelurahan.nama)
        total_all_data = kelurahan.count()
        next_offset =  offset + limit if offset + limit < total_all_data else 0 
        prev_offset = offset - limit if offset - limit > 0 else 0
        
        # check offset and limit argument
        await check_limit_and_offset(kelurahan,limit=limit,offset=offset)
        kelurahan = kelurahan.limit(limit).offset(offset)


    data = {
        'list': kelurahan.all()
    }
    return GetAllKelurahanResponseModel(
        data=data,
        total=kelurahan.count(),
        limit=limit,
        message=strings.DATA_SUCCESS,
        next_offset=next_offset,
        prev_offset=prev_offset,
        total_all_data=total_all_data
    )