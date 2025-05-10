from fastapi import APIRouter, Query
import requests

router = APIRouter()

YOUTUBE_API_KEY = "AIzaSyC3ekTJ_FeG1kJUIcikh7ybkFm6Uk64Xe8"

@router.get("/youtube_search")
def youtube_search(q: str = Query(..., description="検索キーワード")):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": q,
        "type": "video",
        "maxResults": 5,
        "key": YOUTUBE_API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()
