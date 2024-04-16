from fastapi import FastAPI
from routes import flight_booking_router

app = FastAPI()
app.include_router(flight_booking_router)