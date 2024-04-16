from fastapi import FastAPI, Depends
from sqlmodel import SQLModel,Field,Session, create_engine
from typing import Annotated
from dependency import get_session 


app = FastAPI()

class User(SQLModel):
    name:str
    age: int
    gender:str
    is_married: bool
    

class D_User(User, table= True):
    id:int |None =  Field (default= None,primary_key=True)
    name:str
    age:int
    gender: str
    is_married: str

sqlite_file_name = "database.db"
sqlite_url =  f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url,echo = True)
SQLModel.metadata.create_all(engine)


@app.post("/user/")
async def create_user(user:User,session:Annotated[Session, Depends(get_session)]):
    with Session (engine) as session:
        user_1 = User(name = user.name,age = user.age,gender = user.gender,is_married = user.is_married)
        session.add(user_1)
        session.commit()
    return {"name":user.name,"age":user.age,"gender":user.gender, "is_married":user.is_married}

@app.get("/users")
async def get_user(users:User):
    with Session(engine) as session:
        users_1 = session.exec(D_User).all()
    return users_1



