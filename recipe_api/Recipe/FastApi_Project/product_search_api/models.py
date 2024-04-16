from pydantic import BaseModel,Field
class Product(BaseModel):
    product_name:str
    category:str
    price: int
    id: int

class Product_Search_Query(BaseModel):
    product_name:str= Field(min_length=1, max_length=50)
    category: str =Field(min_length=1, max_length=50)
    min_price:int = Field (ge=0, le=1000000) 
    max_price:int = Field(ge=0, le=1000000) 

products = [
        
            {"id": 1 ,"product_name":"laptop","category":"New Model","price":15000},
            {"id":2,"product_name":"Gucci","category":"Hand Bag","price":21000},
            
        ]
