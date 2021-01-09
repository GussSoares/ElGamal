from fastapi import FastAPI
from server_app.api.routers import router


app = FastAPI()

app.include_router(router)
