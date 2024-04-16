from fastapi import FastAPI
from routes import  Recipe_router
from services import search_recipes

app = FastAPI()


app.include_router(Recipe_router)
