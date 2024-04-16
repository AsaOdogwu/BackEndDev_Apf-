from pydantic import BaseModel,Field
from pydantic_extra_types.phonenumber import PhoneNumber
from datetime import date

class CreditCard(BaseModel):
    PhoneNumber: int
    name: str
    age: int
    password:int
    account_type = str

class PaymentAmount(BaseModel):
    price:int = Field(..., lt = 100000,description="This is the limit of money you can send!", example=[100000])
    name: str
    password:int = Field(..., lt=12,description="password should not exceed 12",title=["password"],examples=[243657843245])

class ExpirationDate(BaseModel):
    number: int
    name: str
    password: str
    date: date

class Credentials(BaseModel):
    credit_card: CreditCard
    payment_amount: PaymentAmount
    expiration_date: ExpirationDate