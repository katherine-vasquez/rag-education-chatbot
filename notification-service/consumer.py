from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'order_created',
    group_id='notification-group',
    bootstrap_servers='localhost:9092',
    value_deserializer= lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
)

for message in consumer:
    order_details = message.value
    print(f"Notification: New order received - Item ID: {order_details['item_id']}, Quantity: {order_details['quantity']}, Price: {order_details['price']}")
  