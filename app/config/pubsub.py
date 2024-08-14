import os
from google.cloud import pubsub_v1

def get_pubsub_client():
    return pubsub_v1.PublisherClient.from_service_account_json(
        os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    )
