from fastapi import FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router
from app.api_model import http_exception_handler, validation_exception_handler
from app.api.root import root, RootResponseModel




app = FastAPI(
    title='StrayNeko API',
    version='1.0.0'
    )


origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_exception_handler(StarletteHTTPException, handler=http_exception_handler)
app.add_exception_handler(RequestValidationError, handler=validation_exception_handler)

app.add_api_route('/',
    root,
    tags=['Root'],
    response_model=RootResponseModel)
app.include_router(api_router)