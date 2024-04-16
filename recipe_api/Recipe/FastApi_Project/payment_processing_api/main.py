from fastapi import FastAPI
from routes import card_details_router



app = FastAPI()
app.include_router(card_details_router)


