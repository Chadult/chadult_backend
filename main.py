from fastapi import FastAPI, Query
import requests

app = FastAPI(
    title="Rakuten Hotel Search API",
    description="楽天トラベルAPI経由でホテルを検索するためのラッパー",
    version="1.0.0",
    openapi_url="/openapi.json",
    servers=[
        {"url": "https://rakuten-fastapi.onrender.com", "description": "Render deployment"}
    ]
)

APP_ID = "1061479292841937407"  # 忘れずにセット！

@app.get("/hotels")
def get_hotels(lat: float = Query(...), lng: float = Query(...), radius: int = Query(...)):
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
