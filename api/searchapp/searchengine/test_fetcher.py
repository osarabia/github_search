
from unittest.mock import MagicMock
from .fetcher import Fetcher

class MockCache:
    def exists(self, key):
        pass

    def rpush(self, key, data):
        pass

    def expire(self, seconds):
        pass

    def lrange(self, key, start, end):
        pass

class TestFetcher:
    """
    Test Fetcher
    """
    def test_save_to_cache_not_exists(self):
        """
        test save_to_cache key not exists
        """
        # setup
        fake_cache = MagicMock(MockCache)
        fake_cache.exists.return_value = False
        fetcher_instance = Fetcher("", fake_cache)

        # action
        fetcher_instance.save_to_cache("key", "data")

        # assert
        fake_cache.exists.assert_called_once()
        fake_cache.rpush.assert_called_once()
        fake_cache.expire.assert_called_once()

    def test_save_to_cache_key_exists(self):
        """test save_to_cache key already exists"""
        # setup
        fake_cache = MagicMock(MockCache)
        fake_cache.exists.return_value = True
        fetcher_instance = Fetcher("", fake_cache)

        # action
        fetcher_instance.save_to_cache("key", "data")

        # assert
        fake_cache.exists.assert_called_once()
        fake_cache.rpush.assert_called_once()

    def test_from_cache(self):
        """get data from cache"""
        # setup
        fake_cache = MagicMock(MockCache)
        fake_cache.exists.return_value = True
        fake_cache.lrange.return_value = [b'{"name": "name"}']
        fetcher_instance = Fetcher("", fake_cache)

        # action
        _, _, results = fetcher_instance.from_cache("key")

        # assert
        fake_cache.exists.assert_called_once()
        fake_cache.lrange.assert_called_once()
        assert results == [{"name": "name"}]
 
