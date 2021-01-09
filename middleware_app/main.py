from fastapi import FastAPI
from middleware_app.api.routers import router


app = FastAPI()

app.include_router(router)
