from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import SQLModel,Field,create_engine,Session

app = FastAPI()

class HeroCreate(SQLModel):
    name: str 
    secret_name:str
    age: int 

class Hero(HeroCreate, table = True):
    id:int |None =  Field (default= None,primary_key=True)
    name:str
    secret_name:str
    age:int


sqlite_file_name = "database.db"
sqlite_url =  f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url,echo = True)
SQLModel.metadata.create_all(engine)





@app.post("/hero/")
async def create_hero(hero: HeroCreate):
    with Session(engine) as session:
        hero_1 = Hero(name = hero.name,secret_name = hero.secret_name,age = hero.age)
        session.add(hero_1)
        session.commit()

    return {"name":hero.name,"secret_name":hero.secret_name,"age":hero.age}



