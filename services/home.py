from fastapi import APIRouter
from starlette import status
from starlette.responses import RedirectResponse

router = APIRouter()

@router.get(
    path='/',
    responses={
        307: dict()
    },
    status_code=status.HTTP_307_TEMPORARY_REDIRECT
)
async def index() -> RedirectResponse:
    return RedirectResponse(
        url='/redoc',
        status_code=status.HTTP_307_TEMPORARY_REDIRECT
    )
