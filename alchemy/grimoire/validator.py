def validate_ingredients(ingredients: str) -> str:
    validing = ["fire", "water", "earth", "air"]
    for element in validing:
        if (element in ingredients):
            return (f"{ingredients} - VALID")

    return (f"{ingredients} - INVALID")
