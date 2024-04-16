from pydantic import BaseModel,validator, Field
from fastapi.responses import JSONResponse

class CreditCard(BaseModel):
      number: str = Field(min_length=4,max_length=20,description="Credit card number",title="Credit card",examples= [12544566786567656776])

@validator("number")
def validate_credit_card(name,num):
    sum = 0
    num_digits = len(num)
    odd_even = num_digits & 1

    for count in range(num_digits):
        digit = int(num[count])
        if not ((count & 1) ^ odd_even):
                digit = digit * 2
        if digit > 9:
                digit = digit - 9

        sum = sum + digit

        if sum % 10 == 0:
            return num
        raise ValueError('Invalid credit card number')
    
credit_card_data = {"number": "1234567890123456"}
try:
    card = CreditCard(**credit_card_data)
    print("Credit card is valid:", card.number)
except ValueError as e:
    print(e)

