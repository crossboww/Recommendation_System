from django.shortcuts import render
from django.http import JsonResponse
from .utils import recommend_dishes

def recommend_view(request):
    try:
        protein = float(request.GET.get("protein", 0))
        carbs = float(request.GET.get("carbs", 0))
        fat = float(request.GET.get("fat", 0))
        fiber = float(request.GET.get("fiber", 0))

        recommendations = recommend_dishes(protein, carbs, fat, fiber)

        return JsonResponse({"recommendations": recommendations})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
