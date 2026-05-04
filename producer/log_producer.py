from kafka import KafkaProducer
import json,time
producer=KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode())
for item in [{'pipeline':'etl','error':'Schema mismatch'}]:
    producer.send('pipeline_logs',item)
    print(item)
    time.sleep(1)
producer.flush()
