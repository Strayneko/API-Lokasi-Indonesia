from fastapi import APIRouter

from app.api.root import root, RootResponseModel
from app.api.get_provinsi import get_provinsi, GetProvinsiResponseModel
from app.api.get_kabupaten import get_kabupaten, get_all_kabupaten, GetAllKabupatenResponseModel, GetKabupatenResponseModel
from app.api.get_kecamatan import get_kecamatan, get_all_kecamatan, GetKecamatanResponseModel, GetAllKecamatanResponseModel
from app.api.get_kelurahan import get_kelurahan, get_all_kelurahan, GetKelurahanResponseModel, GetAllKelurahanResponseModel
from app.api.search_data import search_data, filter_data, SearchDataResponseModel

# set api route prefix
api_router = APIRouter(prefix='/api')

api_router.add_api_route(
    '/',
    root,
    tags=['Root'],
    response_model=RootResponseModel
)

api_router.add_api_route(
    '/kabupaten/{id_provinsi}',
    get_kabupaten,
    tags=['Kabupaten'],
    response_model=GetKabupatenResponseModel
)

api_router.add_api_route(
    '/kecamatan/{id_kabupaten}',
    get_kecamatan,
    methods=['GET'],
    tags=['Kecamatan'],
    response_model=GetKecamatanResponseModel
)

api_router.add_api_route(
    '/kelurahan/{id_kecamatan}',
    get_kelurahan,
    methods=['GET'],
    tags=['Kelurahan'],
    response_model=GetKelurahanResponseModel
)
api_router.add_api_route(
    '/search/{type}/{id_area}',
    filter_data,
    summary='Filter Data By ID',
    methods=['GET'],
    tags=['Search'],
    response_model=SearchDataResponseModel
)
api_router.add_api_route(
    '/search/{type}',
    search_data,
    methods=['GET'],
    tags=['Search'],
    response_model=SearchDataResponseModel
)


api_router.add_api_route(
    '/provinsi',
    get_provinsi,
    methods=['GET'],
    tags=['provinsi'],
   response_model=GetProvinsiResponseModel
)
api_router.add_api_route(
    '/kabupaten',
    get_all_kabupaten,
    tags=['Kabupaten'],
    response_model=GetAllKabupatenResponseModel
)

api_router.add_api_route(
    '/kecamatan',
    get_all_kecamatan,
    methods=['GET'],
    tags=['Kecamatan'],
    response_model=GetAllKecamatanResponseModel
)

api_router.add_api_route(
    '/kelurahan',
    get_all_kelurahan,
    methods=['GET'],
    tags=['Kelurahan'],
    response_model=GetAllKelurahanResponseModel
)


