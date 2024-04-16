from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models import License
from services import license_inventory



License_router = APIRouter(prefix="/license", tags =["vehicle"])




@License_router.post("/license/")
async def create_vehicle(license:License):
    response = {
        "message":"your message",
        "data": jsonable_encoder(license)
    }
    return JSONResponse(status_code= 201, content=response)


