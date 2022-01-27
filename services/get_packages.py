from fastapi import APIRouter
from starlette import status
from services import connector

router = APIRouter()


@router.get(
    path='/get_package',
    responses={
    404: dict(),
    200: dict()
    },
    status_code=status.HTTP_200_OK
)
async def get_package():
    conn = connector.connector()
    conn.connect()
    list_package = conn.get_packages()
    print(list_package)
    return list_package
