from fastapi import APIRouter
from starlette import status
from services import connector

router = APIRouter()


@router.get(
    path='/get_channels',
    responses={
    404: dict(),
    200: dict()
    },
    status_code=status.HTTP_200_OK
)
async def get_channels():
    conn = connector.connector()
    conn.connect()
    list_channels = conn.get_channels()
    print(list_channels)
    return list_channels
