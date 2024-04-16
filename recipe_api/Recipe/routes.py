from fastapi import APIRouter, HTTPException
from models import BaseModel, Recipe,Ingredient,NutritionalInfo
from typing import Dict

Recipe_router = APIRouter()

@Recipe_router.post("/recipes/", response_model=Recipe)
def create_recipe(recipe: Recipe):
    # Your implementation for creating a recipe
    return recipe

@Recipe_router.get("/recipes/{title}", response_model=Recipe)
def read_recipe(title: str):
    #implementation for reading a recipe
    return {"message": "Recipe was read successfully"}

@Recipe_router.patch("/recipes/{title}", response_model=Recipe)
def update_recipe(title: str, recipe: Recipe):
    #implementation for updating a recipe
    return {"message":"Recipe updated successfully"}

@Recipe_router.delete("/recipes/{title}")
def delete_recipe(title: str):
    #implementation for deleting a recipe
    return {"message": "Recipe deleted successfully"}

@Recipe_router.post("/ingredients/", response_model=Ingredient)
def create_ingredient(ingredient: Ingredient):
    #for creating an ingredient
    return {"message":"Ingredients was created successfully"}

@Recipe_router.get("/ingredients/{name}", response_model=Ingredient)
def read_ingredient(name: str):
    #implementation for reading an ingredient
    return {"message":"Ingredients was read successfully"}
@Recipe_router.patch("/ingredients/{name}", response_model=Ingredient)
def update_ingredient(name: str, ingredient: Ingredient):
    # implementation for updating an ingredient
    return {"message":"Ingredients updated successfully"}

@Recipe_router.delete("/ingredients/{name}")
def delete_ingredient(name: str):
    #implementation for deleting an ingredient
    return {"message":"ingredient was deleted successfully"}



@Recipe_router.post("/nutritional_info/", response_model=NutritionalInfo)
def create_nutritional_info(nutritional_info: NutritionalInfo):
    #implementation for creating nutritional information
    return {"message":"Nutritional info created successfully"}

@Recipe_router.get("/nutritional_info/", response_model=NutritionalInfo)
def read_nutritional_info():
    #implementation for reading nutritional information
    return {"message":"Nutritional info read succesfully"}

@Recipe_router.put("/nutritional_info/", response_model=NutritionalInfo)
def update_nutritional_info(nutritional_info: NutritionalInfo):
    #implementation for updating nutritional information
    return {"message":"Nutritional info updated successfully"}

@Recipe_router.delete("/nutritional_info/")
def delete_nutritional_info():
    #implementation for deleting nutritional information
    return {"message": "Nutritional information deleted successfully"}
