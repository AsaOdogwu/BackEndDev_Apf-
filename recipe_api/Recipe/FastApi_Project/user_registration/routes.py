from fastapi import APIRouter, HTTPException
from models import User_details

user_router = APIRouter()

@user_router.post("/users/")
async def create_user(user:User_details):
     return user
