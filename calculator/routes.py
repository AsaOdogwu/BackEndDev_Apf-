from FastAPI import APIROUTER
from main import app

calc_router = APIROUTER

@calc_router.get("/add/{score}")
async def get_number(score:int):
    return {"score":score}

