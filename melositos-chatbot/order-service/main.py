from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
import json


app = FastAPI()

class Order(BaseModel):


    item_id: int 
    quantity: int 
    price: float
    id: int 
    retries: int = 0

producer = None

def get_producer():
    global producer
    if producer is None:
        producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    return producer

@app.post("/order")
def create_order(order: Order):
    prod = get_producer()
    prod.send('order_created', order.dict())
    prod.flush()
    return {"message": "Order created", "order": order}



@app.get("/")
def service():
    return {"message": "Api is working"}