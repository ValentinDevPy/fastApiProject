from fastapi import FastAPI
from database.database import DATABASE_URL
from api.handlers import router
from databases import Database

database = Database(DATABASE_URL)


def get_application():
    application = FastAPI()
    application.include_router(router)
    return application


app = get_application()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
