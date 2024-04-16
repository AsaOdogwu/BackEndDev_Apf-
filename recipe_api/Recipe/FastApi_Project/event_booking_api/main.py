from fastapi import FastAPI
from routes import book_event_router


app = FastAPI()
app.include_router(book_event_router)