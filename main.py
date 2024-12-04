import os
from fastapi import FastAPI
from redis import Redis
import datetime

REDIS_URL = os.getenv('REDIS_URL')
# Create a database connection
try:
    redis_connection = Redis.from_url(REDIS_URL)
except ConnectionError as e:
    print("error:", e)

app = FastAPI()


@app.get("/")
def get_last_connection():
    # Get the last time connection from database
    last_connection_old = redis_connection.get("last-connection")
    
    # Get current time
    current_time = datetime.datetime.now()

    # Set time connection in database
    redis_connection.set("last-connection", str(current_time))

    return {"last-connection": last_connection_old}
