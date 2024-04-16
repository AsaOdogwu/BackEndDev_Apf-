# Recipe API

This API allows users to manage recipes, ingredients, and nutritional information.

## Endpoints

### Recipes .This is applicable to the other routes like;ingredients and nutritional information. 
- `POST /recipes/`: Create a new recipe
- `GET /recipes/{title}`: Get a recipe by title
- `PATCH /recipes/{title}`: Update a recipe by title
- `DELETE /recipes/{title}`: Delete a recipe by title

### Filtering and Searching
- `GET /recipes/`: Search for recipes by title
- `GET /recipes/filter/`: Filter recipes by dietary preferences (e.g., vegetarian, gluten-free, low-calorie)

### API Documentation
API documentation is available at `/docs`.

## Third-Party APIs
None used.

## Running the API
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `uvicorn main:app --reload`

## Testing
1.
2. Run tests: `pytest`
