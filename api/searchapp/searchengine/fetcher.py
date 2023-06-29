import logging
import json

from typing import List, Tuple
from .cache import start_redis_client
from .api_puller import GithubApi


class Fetcher:
    """
    Fetcher from Different Data Sources
    """
    def __init__(self, api=None, cache=None):
        """
        Initializing all data sources
        """
        self.api, self.cache = api, cache
        if self.cache is None:
            self.cache = start_redis_client()

        if self.api is None:
            self.api = GithubApi()

    def save_to_cache(self, key, data):
        """
        caching response from github api
        """
        try:
            data = [json.dumps(d) for d in data]
            if not self.cache.exists(key):
                self.cache.rpush(key, *data)
                self.cache.expire(key, 6400)
            else:
                self.cache.rpush(key, *data)
        except Exception as exception:
            error = f"fetcher|when caching|{exception}"
            logging.error(error)

    def from_cache(self, key) -> Tuple[str, bool, List]:
        """
        fetch from cache source
        """
        error, exists, result = "", False, []
        try:
            exists = self.cache.exists(key)
        except Exception as exception:
            error = f"fetcher|cache-error|{exception}"
            logging.error(error)
            return error, exists, result

        if not exists:
            return error, exists, result
        try:
            result = self.cache.lrange(key, 0, -1)
        except Exception as exception:
            error = f"fetcher|cache-error|{exception}"
            logging.error(error)
            return error, exists, []

        return "", exists, [json.loads(r) for r in result]

    def from_api(self, search_input, entity_type) -> Tuple[str, List]:
        """
        fetch requesting data to consumer api
        """
        error, results = self.api.do_request(search_input, entity_type)
        if len(error) == 0 and len(results) > 0:
            key = f"{entity_type}-{search_input}"
            self.save_to_cache(key, results)
        return error, results

    def fetch(self, search_input, entity_type) -> Tuple[str, List]:
        """
        fetch data from cache or from github api
        """
        key = f"{entity_type}-{search_input}"
        print("fetch")
        error, in_cache, result = self.from_cache(key)
        if in_cache:
            return error, result
        error, result = self.from_api(search_input, entity_type)
   
        return error, result