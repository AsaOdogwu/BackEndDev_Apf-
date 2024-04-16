from fastapi import FastAPI
from routes import License_router


app = FastAPI()
app.include_router(License_router)


