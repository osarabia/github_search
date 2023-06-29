
import json
import pytest
import fakeredis
import requests
import responses
import time
import timeit
from searchengine.fetcher import Fetcher
from searchengine.api_puller import GithubApi

setup_data = [
            {
                "login": "osarabia",
                "id": 3688485,
                "node_id": "MDQ6VXNlcjM2ODg0ODU=",
                "avatar_url": "https://avatars.githubusercontent.com/u/3688485?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/osarabia",
                "html_url": "https://github.com/osarabia",
                "followers_url": "https://api.github.com/users/osarabia/followers",
                "following_url": "https://api.github.com/users/osarabia/following{/other_user}",
                "gists_url": "https://api.github.com/users/osarabia/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/osarabia/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/osarabia/subscriptions",
                "organizations_url": "https://api.github.com/users/osarabia/orgs",
                "repos_url": "https://api.github.com/users/osarabia/repos",
                "events_url": "https://api.github.com/users/osarabia/events{/privacy}",
                "received_events_url": "https://api.github.com/users/osarabia/received_events",
                "type": "User",
                "site_admin": False,
                "score": 1.0
            },
            {
                "login": "OSarabia7",
                "id": 41201745,
                "node_id": "MDQ6VXNlcjQxMjAxNzQ1",
                "avatar_url": "https://avatars.githubusercontent.com/u/41201745?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/OSarabia7",
                "html_url": "https://github.com/OSarabia7",
                "followers_url": "https://api.github.com/users/OSarabia7/followers",
                "following_url": "https://api.github.com/users/OSarabia7/following{/other_user}",
                "gists_url": "https://api.github.com/users/OSarabia7/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/OSarabia7/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/OSarabia7/subscriptions",
                "organizations_url": "https://api.github.com/users/OSarabia7/orgs",
                "repos_url": "https://api.github.com/users/OSarabia7/repos",
                "events_url": "https://api.github.com/users/OSarabia7/events{/privacy}",
                "received_events_url": "https://api.github.com/users/OSarabia7/received_events",
                "type": "User",
                "site_admin": False,
                "score": 1.0
            }
]


def request_callback(request):
    """slow http request"""
    time.sleep(3)  # delay for 2 seconds
    return (200, {}, json.dumps({'items': [setup_data[0], setup_data[1]]}))


def test_fetcher_instance():
    """
    Test Fetch instance
    """
    # action
    fetcher = Fetcher("", "")
    # assert
    assert isinstance(fetcher, Fetcher)


def test_fetcher_data_from_redis():
    """
    Fetch from Redis
    """

    # arrange
    entity_type = "users"
    search_criteria = "omar"
    key = f"{entity_type}-{search_criteria}"
    data = setup_data

    cache = fakeredis.FakeStrictRedis()

    cache.rpush(key, json.dumps(data[0]), json.dumps(data[1]))
    fetcher = Fetcher("", cache)

    # action
    _, result = fetcher.fetch(search_criteria, entity_type)

    # assert
    assert result == data


@responses.activate
def test_fetcher_caching_data():
    """
    Fetch First
    Then Caching
    """

    # arrange
    entity_type = "users"
    search_criteria = "omar"
    key = f"{entity_type}-{search_criteria}"
    data = setup_data

    cache = fakeredis.FakeStrictRedis()

    responses.add(responses.GET, 'https://api.github.com/search/users?q=omar',
                  json={
                      'items': [data[0], data[1]]
                      }, status=200)

    api_puller = GithubApi()

    fetcher = Fetcher(api_puller, cache)

    # action
    _, result = fetcher.fetch(search_criteria, entity_type)

    # assert
    assert cache.exists(key)
    assert len(cache.lrange(key, 0, -1)) == 2

@responses.activate
def test_fetcher_full_round():
    """
    Full Round Fetch    
    """

    # arrange
    entity_type = "users"
    search_criteria = "omar"

    cache = fakeredis.FakeStrictRedis()

    responses.add_callback(
        responses.GET, 
        'https://api.github.com/search/users?q=omar',
        callback=request_callback,
        content_type='application/json')

    api_puller = GithubApi()

    fetcher = Fetcher(api_puller, cache)

    # action
    first_start_time = timeit.default_timer()
    _, first_call_result = fetcher.fetch(search_criteria, entity_type)
    first_end_time = timeit.default_timer()
    first_execute_time = first_end_time - first_start_time

    second_start_time = timeit.default_timer()
    _, second_call_result = fetcher.fetch(search_criteria, entity_type)
    second_end_time = timeit.default_timer()
    second_execute_time = second_end_time - second_start_time

    # assert
    assert first_execute_time > second_execute_time
    assert first_call_result == second_call_result