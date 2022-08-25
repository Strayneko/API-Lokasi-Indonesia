# invalid argument error
from fastapi.exceptions import HTTPException
from starlette import status

from app.utils import strings

async def check_limit_and_offset(object, limit, offset):
        if object.count() == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=strings.NO_DATA_FOUND
            )
        
        if limit >= object.count():
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail=strings.LIMIT_EXCEEDED
            )
        
        if limit > 0:
            next_offset =  offset + limit if offset + limit < object.count() else 0
            object = object.offset(offset).limit(limit)

            if next_offset == 0:
                raise HTTPException(
                    status_code=status.HTTP_200_OK,
                    detail=strings.OFFSET_EXCEEDED
                )

        if offset > 0 and limit == 0:
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail=strings.LIMIT_NOT_SPECIFIED
            )


