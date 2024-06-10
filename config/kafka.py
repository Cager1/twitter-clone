# kafka/kafka_handler.py
import asyncio
import os

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS',)
TOPIC_NAME = 'tweets'

async def produce_tweet(tweet: str):
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        await producer.send_and_wait(TOPIC_NAME, tweet.encode('utf-8'))
    finally:
        await producer.stop()

async def consume_tweets():
    consumer = AIOKafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id="tweet-group",
        auto_offset_reset="earliest"
    )
    await consumer.start()
    try:
        async for msg in consumer:
            yield msg.value.decode('utf-8')
    finally:
        await consumer.stop()
