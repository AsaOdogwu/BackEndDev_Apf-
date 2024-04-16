from pydantic import BaseModel, EmailStr,Field
from datetime import date
from pydantic_extra_types.phone_numbers import PhoneNumber


class Vehiclecheck(BaseModel):
    name: str = Field(min_length=10, max_length=25,description="name of the vehicle owner",examples=["Okonkwo Daniel Emesiobi"],title="Name")
    age: int = Field(gt=0, lt=120, description="Age of the passenger", examples=[25], title="Age") # noqa
    email: EmailStr
    phone: PhoneNumber= Field(description="Phone number of the vehicle owner",examples=["+23489897679"],title="phone")    

class  Vehiclepattern(BaseModel):
    make: str = Field(min_length=4,max_length=6,description="This name is  the  make of this vehicle",examples=["Toyota"],title="make")

    model_year: date = Field(...,description="this is the model of the vehicle",examples=["2024-01-24"],title="model_year")

    color: str= Field(description="This is the color of the car",examples= ["red"], title ="color")

    vin: str= Field(min_length=13,max_length=13,description="this is the unique VIN number",title="VIN",examples=["A-KS-GUR-W4-8"])

    condition: str =Field(description="The condition of the vehicle,either used or not", examples=["Used"],title="condition")

    mileage: str=Field(min_length=2,max_length=5,description="This is the distance of the car",
    examples=["100km"], title="mileage")
                       
    price: str=Field(min_length=5,max_length=9,description="This is the the price of the car",examples=["$10000.00"],title="price")

class License(BaseModel):
    vehicleCheck: Vehiclecheck
    vehiclePattern: Vehiclepattern
