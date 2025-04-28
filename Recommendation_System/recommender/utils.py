import json
import os

def load_dishes():
    """Load all dishes from the JSON file."""
    path = os.path.join(os.path.dirname(__file__), 'data', 'dish_name.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_dishes = []
    for restaurant in data:
        for dish in restaurant.get('menu', []):
            all_dishes.append({
                'dish_name': dish.get('dish_name', ''),
                'protein': float(dish.get('protein', 0) or 0),
                'carbs': float(dish.get('carbs', 0) or 0),
                'fat': float(dish.get('fat', 0) or 0),
                'fiber': float(dish.get('fiber', 0) or 0),
            })
    return all_dishes

def recommend_dishes(user_protein, user_carbs, user_fat, user_fiber, max_difference=10):
    """Recommend dishes closest to user requirements."""
    dishes = load_dishes()
    recommendations = []

    for dish in dishes:
        difference = (
            abs(dish['protein'] - user_protein) +
            abs(dish['carbs'] - user_carbs) +
            abs(dish['fat'] - user_fat) +
            abs(dish['fiber'] - user_fiber)
        )
        recommendations.append((difference, dish))

    recommendations.sort(key=lambda x: x[0])

    good_matches = [dish for diff, dish in recommendations if diff <= max_difference]

    if good_matches:
        return good_matches

    # Step 2: If no good matches, return top 5 closest dishes
    return [dish for _, dish in recommendations[:5]]

