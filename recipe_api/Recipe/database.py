from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel,requests
from typing import List, Optional


app = FastAPI()

# Mock database for demonstration purposes
recipes_db = {}

class Recipe(BaseModel):
    title: str
    ingredients: List[str]

@app.post("/recipes/", response_model=Recipe)
def create_recipe(recipe: Recipe):
    recipes_db[recipe.title] = recipe
    return recipe

@app.get("/recipes/{title}", response_model=Recipe)
def read_recipe(title: str):
    if title not in recipes_db:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes_db[title]

# Function to fetch nutritional data from a hypothetical food database API
def fetch_nutritional_data(ingredient: str) -> dict:
    # Hypothetical food database API endpoint
    api_url = f"https://api.food-database.com/ingredient/{ingredient}"
    # Make HTTP GET request to API
    response = requests.get(api_url)
    # Check if request was successful
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch nutritional data")
    # Extract nutritional data from API response
    nutritional_data = response.json()
    return nutritional_data

# Function to calculate nutritional information for a recipe based on its ingredients
def calculate_nutritional_info(ingredients: List[str]) -> dict:
    nutritional_info = {
        "calories": 0,
        "fat": 0,
        "protein": 0,
        "carbohydrates": 0
    }
    for ingredient in ingredients:
        # Fetch nutritional data for each ingredient from the food database API
        ingredient_data = fetch_nutritional_data(ingredient)
        # Aggregate nutritional information
        nutritional_info["calories"] += ingredient_data.get("calories", 0)
        nutritional_info["fat"] += ingredient_data.get("fat", 0)
        nutritional_info["protein"] += ingredient_data.get("protein", 0)
        nutritional_info["carbohydrates"] += ingredient_data.get("carbohydrates", 0)
    return nutritional_info

# Endpoint to calculate and return the nutritional information for a recipe
@app.get("/recipes/{title}/nutritional_info")
def get_nutritional_info(title: str):
    if title not in recipes_db:
        raise HTTPException(status_code=404, detail="Recipe not found")
    recipe = recipes_db[title]
    nutritional_info = calculate_nutritional_info(recipe.ingredients)
    return {"recipe": title, "nutritional_info": nutritional_info}
