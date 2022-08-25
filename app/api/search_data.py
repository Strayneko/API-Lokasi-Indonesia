from operator import contains
from app.utils.api_dependencies import *
from app.models.Provinsi import Provinsi
from app.models.Kabupaten import Kabupaten
from app.models.Kecamatan import Kecamatan
from app.models.Kelurahan import Kelurahan

class SearchDataResponseModel(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'code': status.HTTP_200_OK,
                'status': True,
                'message': 'success',
                'total':1,
                'data': {
                    'type': 'kabupaten', 
                    'list': [{
                    'id': 214,
                    'nama': 'Pemalang',
                }],
                },
             
            }
        }

async def search_data(type: str = '', keyword: str = ''):
    if keyword == '':
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail=strings.KEYWORD_REQUIRED
        )
        
    with Session(db_engine) as session:
        # determine model for each area type
        match type:
            case 'provinsi':
                data = session.query(Provinsi.id, Provinsi.nama).filter(Provinsi.nama.contains(keyword))
            case 'kabupaten':
                data = session.query(Kabupaten.id, Kabupaten.nama, Kabupaten.id_provinsi).filter(Kabupaten.nama.contains(keyword))
            case 'kecamatan':
                data = session.query(Kecamatan.id, Kecamatan.nama, Kecamatan.id_kabupaten).filter(Kecamatan.nama.contains(keyword))
            case 'kelurahan':
                data = session.query(Kelurahan.id, Kelurahan.nama, Kelurahan.id_kecamatan).filter(Kelurahan.nama.contains(keyword))
            case default:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=strings.AREA_TYPE_NOT_FOUND
                )


    if data.count() == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.NO_DATA_FOUND
        )
    return SearchDataResponseModel(
        total=data.count(),
        message=strings.DATA_SUCCESS,
        data={
            'type':type,
            'list': data.all()
            }
    )


async def filter_data(type: str = '', id_area: int = 0):
    with Session(db_engine) as session:
        # determine model for each area type
        match type:
            case 'provinsi':
                data = session.query(Provinsi.id, Provinsi.nama).filter(Provinsi.id==id_area)
            case 'kabupaten':
                data = session.query(Kabupaten.id, Kabupaten.nama, Kabupaten.id_provinsi).filter(Kabupaten.id==id_area)
            case 'kecamatan':
                data = session.query(Kecamatan.id, Kecamatan.nama, Kecamatan.id_kabupaten).filter(Kecamatan.id==id_area)
            case 'kelurahan': 
                data = session.query(Kelurahan.id, Kelurahan.nama, Kelurahan.id_kecamatan).filter(Kelurahan.id==id_area)
                
            case default:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=strings.AREA_TYPE_NOT_FOUND
                )

    if data.count() == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.NO_DATA_FOUND
        )
    
    return SearchDataResponseModel(
        message=strings.DATA_SUCCESS,
        total=data.count(),
        data={
            'type':type,
            'list': data.all()
            }
    )