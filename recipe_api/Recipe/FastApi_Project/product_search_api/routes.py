from fastapi import APIRouter
from fastapi.responses import JSONResponse
from routes import check_products_router
from models import products,List


check_products_router = APIRouter



@check_products_router.get("/product_search/",response_model = List[Product])
async def search_products(query_params: product_search_query = Query()):

    results = products

    if query_params.product_name:
        results = [p for p in results if query_params.product_name.lower() in p ["product_name"].lower()]

    if query_params.category:
        results = [p for p in results if query_params.category.lower() in p ["category"].lower()]

    if query_params.min_price is not None:
        results = [p for p in results if p ["price"] >= query_params.min_price]

    if query_params.max_price is not None:
        results = [p for p in results if p ["price"] <= query_params.max_price]
    return results    
   