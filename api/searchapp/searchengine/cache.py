import os
import logging
import redis


def start_redis_client() -> redis.Redis:
    """
    Start Redis Client
    """
    return redis.Redis(
                host=os.getenv('REDIS_HOST', 'localhost'),
                port=int(os.getenv('REDIS_PORT', '6379')),
                db=0
            )


def flush_everything():
    """
    Flush Cache
    """
    try:
        redis_client = start_redis_client()
        redis_client.flushdb()
    except Exception as exception:
        error = f"unable_to_flush_cache|{exception}"
        logging.error(error)