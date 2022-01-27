from fastapi import APIRouter
from starlette import status
from services import connector

router = APIRouter()

@router.put(
    path='/put_package/subscription_type/{subscription_type}/price/{price}/channels_list/{channels_list}',
    responses={
    404: dict(),
    200: dict()
    },
    status_code=status.HTTP_200_OK
)
async def put_package(subscription_type, price, channels_list):
    conn = connector.connector()
    conn.connect()
    list_package = conn.put_package(subscription_type, price, channels_list)
    print(list_package)
    return 'success'