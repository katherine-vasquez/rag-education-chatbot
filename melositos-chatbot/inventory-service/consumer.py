from kafka import KafkaConsumer
import json 


consumer = KafkaConsumer(
    'order_created', # Canal de escucha entre order
    group_id='inventory-group', # Identificador del grupo de consumidores
    bootstrap_servers='localhost:9092', # Dirección del servidor Kafka
    value_deserializer= lambda m:  json.loads(m.decode('utf-8')), # Deserializador de mensajes
    auto_offset_reset='earliest', # Desde dónde empezar a leer mensajes
    enable_auto_commit=True, # Confirmar automáticamente la lectura de mensajes

)

for message in consumer:
    order_id = message.value['item_id']
    print(f"Received order with ID: {order_id}")    # Aquí se podría agregar lógica para actualizar el inventario basado en la orden recibida