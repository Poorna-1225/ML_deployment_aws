import json
import requests

input_data = {
  "pregnancies": 10,
  "Glucose": 100,
  "BloodPressure": 50,
  "SkinThickness": 20,
  "Insulin": 110,
  "BMI": 15,
  "DiabetesPedigreeFunction": 0.56,
  "Age": 40
}

url = "http://localhost/diabetes_prediction" # sometimes the original url doesn't work then use localhost/docs to open swagger

response = requests.post(url, data= json.dumps(input_data))

print(response.text)