import responses
from .api_puller import GithubApi


class TestApiPuller:

    @responses.activate
    def test_do_request(self):
        # setup
        api = GithubApi()
        data = [
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
        responses.add(responses.GET, 'https://api.github.com/search/users?q=omar', 
                      json={'items': [data[0], data[1]]}, status=200)
        
        search_criteria = "omar"
        entity_type = "users"

        # action
        error, result = api.do_request(search_criteria, entity_type)

        assert error == ""
        assert len(result) == 2

