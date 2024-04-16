from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from routes import check_product_router

app = FastAPI()

app.include_router(check_product_router)



#Product Search API:
#  Develop a FastAPI endpoint for searching products.
#  Accept query parameters for product name, category, and price range.
#  Implement string validation for product name and category.
#  Apply numeric validation for price range parameters.
#  Return a list of products matching the search criteria.
#  Test the API with various combinations of query parameters.



   

