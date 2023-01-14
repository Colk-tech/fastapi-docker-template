from fastapi import FastAPI

from sample.routers import hello

app = FastAPI()
app.include_router(hello.router)
