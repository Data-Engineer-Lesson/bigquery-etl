from fastapi import APIRouter,HTTPException,Request
from app.config.pubsub import get_pubsub_client
from app.config.logger import logger
import json

router = APIRouter()

@router.post('/log')
async def insert_log(request: Request):
    event = await request.json()
    pubsub_client = get_pubsub_client()

    try:
        topic_path = pubsub_client.topic_path('collecting-events-430021', 'event-logs-topic')
        pubsub_client.publish(topic_path, json.dumps(event).encode("utf-8"))
        logger.info("Event published to pubsub")
        return {'message': "Event published"}
    except Exception as e:
        logger.info(f"Error published to pubsub {e}")
        raise HTTPException(status_code=500)
        