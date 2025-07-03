from fastapi import FastAPI
from redis import Redis
import json

app = FastAPI()

@app.on_event('startup')
async def startup():
    app.state.redis = Redis(host='localhost', port=6379)

@app.get('/')
async def data():
    data = app.state.redis.get('dog')
    
    if not data:
        return {"error": "No data found"}

    return {"dog": data}