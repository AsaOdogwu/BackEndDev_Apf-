from pydantic import BaseModel,EmailStr, Field


class User_details(BaseModel):
    username: str = Field(min_length= 4,max_length= 30,description="Username of user",examples=["kokolet"],title="username",pattern="^[a-zA-Z]+$")
    password: str = Field(...,max_length=8,description="password of the user",examples=["gu123!E"])
    phone: str = Field(...,max_length=15, description="phone number of the user",examples=["+234-8122811459"])
    gender: str = Field(..., description="the gender of the user",examples=["Male"])
    country: str = Field(min_length=4,max_length= 20,description="The country of the user",examples=["Nigeria"])

