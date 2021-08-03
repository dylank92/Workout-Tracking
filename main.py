import requests
from datetime import datetime
import os
from requests.auth import HTTPBasicAuth



SHEETY_ENDPOINT = f"https://api.sheety.co/d999bafebc13b3de3f1b436b5bb28aea/myWorkouts/workouts"
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
GENDER = "Female"
WEIGHT_KG = "75.5"
HEIGHT_CM = "165.5"
AGE = "30"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise = input("What exercise did you do today?: ")

workout_config = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
response = requests.post(url=API_ENDPOINT, json=workout_config, headers=headers)
result = response.json()

print(result)

date = datetime.now()
today = date.strftime("%d/%m/%Y")
hour = date.strftime("%X")

# for loop to pull from sheet_inputs:
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": hour,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }


#Basic Authentication and pull JSON data from sheet_inputs
    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, auth=(USERNAME, PASSWORD))
    print(sheet_response.text)

