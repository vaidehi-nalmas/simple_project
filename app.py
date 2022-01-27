from fastapi import FastAPI, APIRouter

from services import get_channels, get_packages, post_package, home

app = FastAPI(
    title='DTH CHANNELS',
    description='Displays channels list and provides provision to add or modify channels packages',
    openapi_url=f'/openapi.json',
    redoc_url=f'/redoc'
)

router = APIRouter()

app.include_router(home.router)
app.include_router(get_channels.router)
app.include_router(post_package.router)
app.include_router(get_packages.router)

if __name__ == "__main__":
    import uvicorn
    app.debug = True
    uvicorn.run(
        app=app,
        debug=app.debug
    )