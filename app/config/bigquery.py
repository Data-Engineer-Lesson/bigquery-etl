import os
from google.cloud import bigquery

def get_bigquery_client():
    return bigquery.Client.from_service_account_json(
        os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    )
