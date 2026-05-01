from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'order_created.DLQ',
    group_id='log-group',
    bootstrap_servers='localhost:9092',
    value_deserializer= lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
)


for message in consumer:
    order_details = message.value
    print(f"Log Service: Order not processed - Data: {order_details} | Error: {order_details.get('Error')}")