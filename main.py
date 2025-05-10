from fastapi import FastAPI, Query
import requests

app = FastAPI()

APP_ID = "1061479292841937407"  # ← ここにアプリIDを""付きで貼ってください（例："1234567890"）

@app.get("/hotels")
def get_hotels(lat: float = Query(...), lng: float = Query(...), radius: int = Query(3)):
    url = "https://app.rakuten.co.jp/services/api/Travel/SimpleHotelSearch/20170426"
    params = {
        "applicationId": APP_ID,
        "format": "json",
        "latitude": lat,
        "longitude": lng,
        "searchRadius": radius,
        "datumType": 1,
        "hits": 5
    }
    response = requests.get(url, params=params)
    return response.json()
