import streamlit as st
import requests

st.title("Dish Recommender System")

protein = st.number_input("Protein", min_value=0.0)
carbs = st.number_input("Carbs", min_value=0.0)
fat = st.number_input("Fat", min_value=0.0)
fiber = st.number_input("Fiber", min_value=0.0)

if st.button("Recommend Dishes"):
    url = "http://127.0.0.1:8000/recommend/"
    params = {
        "protein": protein,
        "carbs": carbs,
        "fat": fat,
        "fiber": fiber
    }

    # Debugging: Print URL and Params
    print("URL:", url)
    print("Params:", params)

    try:
        res = requests.get(url, params=params)
        res.raise_for_status()  # Will raise an HTTPError for bad responses
        data = res.json()

        if "recommendations" in data:
            for dish in data["recommendations"]:
                st.write(f"{dish['dish_name']} - Protein: {dish['protein']}, Carbs: {dish['carbs']}, Fat: {dish['fat']}, Fiber: {dish['fiber']}")
        else:
            st.warning("No dishes found.")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
