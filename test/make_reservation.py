import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERVICE_URL = os.getenv("SERVICE_URL")
endpoint = "reservations"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiY3N0cm51bGwwMCIsImV4cCI6MTY4NzA3NDQ3M30.vPKcFz88BKpj5rRscnDB9wJFDbXYDR_mIq9AAwYPSnU"
    }
reservation_data = {
    "user_id": "cstrnull00",
    "stadium_id": "648ea91a644962fa656fb9d3",
    "date": "2023-06-21",
    "time": ["13:30", "16:00"]
}

url = SERVICE_URL + endpoint

# POST 요청 보내기
response = requests.post(url, json=reservation_data, headers=headers)

# 응답 확인
if response.status_code == 201:
    print("Reservation created successfully.")
else:
    print(response.text)
