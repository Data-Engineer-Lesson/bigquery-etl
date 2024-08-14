import logging

logger = logging.getLogger('fastapi_collecting_events')
logger.setLevel(logging.INFO)

handler= logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))

file_handler = logging.FileHandler('combined.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))

logger.addHandler(handler)
logger.addHandler(file_handler)