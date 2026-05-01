from kafka import KafkaConsumer
import json
import time
from producer_dql import producer

consumer = KafkaConsumer(
    "order_created",
    group_id="notification",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=False
)

MAX_RETRIES = 3

for message in consumer:
    data = message.value
    retries = data.get("retries", 0)

    try:
        if data["id"] % 2 == 0:
            raise Exception("Simulated error")

        print(f"Shipment OK for order {data['id']}")
        consumer.commit()

    except Exception as e:
        retries += 1
        data["retries"] = retries

        if retries < MAX_RETRIES:
            time.sleep(10)
            producer.send("order_created", data)
            producer.flush()
            consumer.commit()
            print(f"Retry {retries}/{MAX_RETRIES}")

        else:

            error = str(e)
            data["error"] = error
            
            producer.send("order_created.DLQ", data)
            producer.flush()
            consumer.commit()
            print("Sent to DLQ")
