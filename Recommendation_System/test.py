import sys
import os

# Path set karo
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from recommender.utils import recommend_dishes

# User ki nutrition requirement
user_protein = 28
user_carbs = 15
user_fat = 6
user_fiber = 7

# Recommend dishes
recommended = recommend_dishes(user_protein, user_carbs, user_fat, user_fiber)

# Show recommendations
if recommended:
    for dish in recommended:
        print(dish)
else:
    print("No matching dishes found.")
