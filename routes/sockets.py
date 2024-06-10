# routes/sockets.py
from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketDisconnect
from config.kafka import consume_tweets
from app.http.helpers.user_helper import get_user_by_session
import json
router = APIRouter()


@router.websocket("/ws/tweets")
async def websocket_endpoint(websocket: WebSocket):
    tweets = consume_tweets()
    await websocket.accept()
    try:
        async for tweet in tweets:
            print(tweet)
            await websocket.send_text(tweet)
    except WebSocketDisconnect:
        print("Client disconnected")
        await websocket.close()
