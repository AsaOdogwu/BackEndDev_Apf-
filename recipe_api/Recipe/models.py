from pydantic import BaseModel,Field
from typing import List

class NutritionalInfo(BaseModel):
    calories: float
    fat: float
    protein: float

class Ingredient(BaseModel):
    name: str
    quantity: float
    nutritional_info: NutritionalInfo

class Recipe(BaseModel):
    title: str
    description: str
    instructions: str
    ingredients: List[Ingredient]
    nutritional_info: NutritionalInfo