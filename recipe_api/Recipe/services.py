from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()

# Actual recipe details
recipes = [
    {
        "title": "Spaghetti Bolognese",
        "ingredients": ["spaghetti", "ground beef", "onion", "garlic", "tomato sauce"],
        "nutritional_info": {
            "calories": 480,
            "fat": 22,
            "protein": 30,
            "carbohydrates": 45
        },
        "dietary_preferences": ["gluten-free"]
    },
    {
        "title": "Caprese Salad",
        "ingredients": ["tomatoes", "mozzarella cheese", "fresh basil", "balsamic vinegar", "olive oil"],
        "nutritional_info": {
            "calories": 250,
            "fat": 20,
            "protein": 10,
            "carbohydrates": 5
        },
        "dietary_preferences": ["low-calorie"]
    },
    {
        "title": "Crispy cauliflower and chickpea tacos ",
        "ingredients":["smoky paprika", "zesty lime juice", "freshly ground black pepper","vegan chipotle lime crema","crunchy slaw"],
        "nutritional_info":{
            "calories":1406,
            "fat": "72g",
            "protein": "33g"
        },
        "dietary_prefernces": ["vegetarian"]
    }
]

# Endpoint for searching and filtering recipes
@app.get("/recipes")
def search_recipes(
    title: Optional[str] = None,
    ingredients: Optional[str] = None,
    diet: Optional[str] = None,
    max_calories: Optional[int] = None
):
    filtered_recipes = recipes

    # Filter by title
    if title:
        filtered_recipes = [recipe for recipe in filtered_recipes if title.lower() in recipe["title"].lower()]

    # Filter by ingredients
    if ingredients:
        ingredient_list = ingredients.split(",")
        filtered_recipes = [
            recipe for recipe in filtered_recipes if all(ingr in recipe["ingredients"] for ingr in ingredient_list)
        ]

    # Filter by dietary preferences
    if diet:
        dietary_list = diet.split(",")
        filtered_recipes = [
            recipe for recipe in filtered_recipes if any(pref in recipe["dietary_preferences"] for pref in dietary_list)
        ]

    # Filter by maximum calories
    if max_calories is not None:
        filtered_recipes = [recipe for recipe in filtered_recipes if recipe["nutritional_info"]["calories"] <= max_calories]

    return {"recipes": filtered_recipes}

