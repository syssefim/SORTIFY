from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the data structure you expect to receive
class PhoneData(BaseModel):
    message: str
    battery_level: int

@app.post("/receive-data")
async def receive_data(data: PhoneData):
    print(f"Received from phone: {data.message}, Battery: {data.battery_level}%")
    return {"status": "success", "received": data}