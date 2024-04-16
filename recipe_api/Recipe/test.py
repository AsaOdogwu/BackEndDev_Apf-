from fastapi import FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import OpenAPI
import pytest
from fastapi.testclient import TestClient
import app
import Recipe_router


app = FastAPI()

client = TestClient(app)



# To include your routers
app.include_router(Recipe_router)

# Generate API documentation using Swagger UI
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API documentation")

# Generate OpenAPI schema
@app.get("/openapi.json", include_in_schema=False)
async def get_openapi():
    return app.openapi()

# cases for recipe endpoints
def test_create_recipe():
    # Send a POST request with valid data
    response = client.post("/recipes/", json={"title": "Test Recipe", "ingredients": ["ingredient1"], "nutritional_info": {"calories": 200, "fat": 10, "protein": 30, "carbohydrates": 30}})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Recipe"

    # POST request with invalid data (missing required fields)
    response = client.post("/recipes/", json={"ingredients": ["ingredient1"], "nutritional_info": {"calories": 200, "fat": 10, "protein": 30, "carbohydrates": 30}})
    assert response.status_code == 422

    # Send a GET request to retrieve the created recipe
    response = client.get("/recipes/Test%20Recipe")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Recipe"

    # Send a GET request for a non-existent recipe
    response = client.get("/recipes/NonExistentRecipe")
    assert response.status_code == 404


# Test cases for error-handling scenarios
def test_error_handling():
    #POST request with invalid JSON payload
    response = client.post("/recipes/", data="Invalid JSON payload")
    assert response.status_code == 422

    # GET request with an invalid endpoint
    response = client.get("/invalid_endpoint")
    assert response.status_code == 404
