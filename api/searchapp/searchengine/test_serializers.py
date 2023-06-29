from .serializers import repository_serializer, user_serializer, issue_serializer


class TestSerializers:
    """
    Test Serializers
    """

    def test_user_serializer(self):
        """
        Test User Serializer
        """
        # setup
        inbound_data = {
            "login": "omar",
            "id": 196368,
            "node_id": "MDQ6VXNlcjE5NjM2OA==",
            "avatar_url": "https://avatars.githubusercontent.com/u/196368?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/omar",
            "html_url": "https://github.com/omar",
            "followers_url": "https://api.github.com/users/omar/followers",
            "following_url": "https://api.github.com/users/omar/following{/other_user}",
            "gists_url": "https://api.github.com/users/omar/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/omar/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/omar/subscriptions",
            "organizations_url": "https://api.github.com/users/omar/orgs",
            "repos_url": "https://api.github.com/users/omar/repos",
            "events_url": "https://api.github.com/users/omar/events{/privacy}",
            "received_events_url": "https://api.github.com/users/omar/received_events",
            "type": "User",
            "site_admin": False,
            "score": 1.0
        }
        expected_keys = set(['profile_picture', 'name', 
                             'profile_url', 'profile_html_url', 
                             'repos_url', 'bio', 'email', 'blog', 
                             'company', 'location', 'id'])
        # action
        serialized_user_data = user_serializer(inbound_data)

        # assert
        assert serialized_user_data.keys() == expected_keys

    def test_repository_serializer(self):
        """
        Test Repository Serializer
        """
        inbound_data = {
                "id": 40453691,
                "node_id": "MDEwOlJlcG9zaXRvcnk0MDQ1MzY5MQ==",
                "name": "GolangTraining",
                "full_name": "GoesToEleven/GolangTraining",
                "private": False,
                "owner": {
                    "login": "GoesToEleven",
                    "id": 8296040,
                    "node_id": "MDQ6VXNlcjgyOTYwNDA=",
                    "avatar_url": "https://avatars.githubusercontent.com/u/8296040?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/GoesToEleven",
                    "html_url": "https://github.com/GoesToEleven",
                    "followers_url": "https://api.github.com/users/GoesToEleven/followers",
                    "following_url": "https://api.github.com/users/GoesToEleven/following{/other_user}",
                    "gists_url": "https://api.github.com/users/GoesToEleven/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/GoesToEleven/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/GoesToEleven/subscriptions",
                    "organizations_url": "https://api.github.com/users/GoesToEleven/orgs",
                    "repos_url": "https://api.github.com/users/GoesToEleven/repos",
                    "events_url": "https://api.github.com/users/GoesToEleven/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/GoesToEleven/received_events",
                    "type": "User",
                    "site_admin": False
                },
                "html_url": "https://github.com/GoesToEleven/GolangTraining",
                "description": "Training for Golang (go language)",
                "fork": False,
                "url": "https://api.github.com/repos/GoesToEleven/GolangTraining",
                "forks_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/forks",
                "keys_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/keys{/key_id}",
                "collaborators_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/collaborators{/collaborator}",
                "teams_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/teams",
                "hooks_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/hooks",
                "issue_events_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/issues/events{/number}",
                "events_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/events",
                "assignees_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/assignees{/user}",
                "branches_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/branches{/branch}",
                "tags_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/tags",
                "blobs_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/git/blobs{/sha}",
                "git_tags_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/git/tags{/sha}",
                "git_refs_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/git/refs{/sha}",
                "trees_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/git/trees{/sha}",
                "statuses_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/statuses/{sha}",
                "languages_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/languages",
                "stargazers_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/stargazers",
                "contributors_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/contributors",
                "subscribers_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/subscribers",
                "subscription_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/subscription",
                "commits_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/commits{/sha}",
                "git_commits_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/git/commits{/sha}",
                "comments_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/comments{/number}",
                "issue_comment_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/issues/comments{/number}",
                "contents_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/contents/{+path}",
                "compare_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/compare/{base}...{head}",
                "merges_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/merges",
                "archive_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/{archive_format}{/ref}",
                "downloads_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/downloads",
                "issues_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/issues{/number}",
                "pulls_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/pulls{/number}",
                "milestones_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/milestones{/number}",
                "notifications_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/notifications{?since,all,participating}",
                "labels_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/labels{/name}",
                "releases_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/releases{/id}",
                "deployments_url": "https://api.github.com/repos/GoesToEleven/GolangTraining/deployments",
                "created_at": "2015-08-09T23:09:58Z",
                "updated_at": "2023-06-27T17:44:53Z",
                "pushed_at": "2023-01-03T13:25:14Z",
                "git_url": "git://github.com/GoesToEleven/GolangTraining.git",
                "ssh_url": "git@github.com:GoesToEleven/GolangTraining.git",
                "clone_url": "https://github.com/GoesToEleven/GolangTraining.git",
                "svn_url": "https://github.com/GoesToEleven/GolangTraining",
                "homepage": None,
                "size": 41659,
                "stargazers_count": 9004,
                "watchers_count": 9004,
                "language": "Go",
                "has_issues": True,
                "has_projects": True,
                "has_downloads": True,
                "has_wiki": True,
                "has_pages": False,
                "has_discussions": False,
                "forks_count": 3415,
                "mirror_url": None,
                "archived": False,
                "disabled": False,
                "open_issues_count": 45,
                "license": {
                    "key": "other",
                    "name": "Other",
                    "spdx_id": "NOASSERTION",
                    "url": None,
                    "node_id": "MDc6TGljZW5zZTA="
                },
                "allow_forking": True,
                "is_template": False,
                "web_commit_signoff_required": False,
                "topics": [

                ],
                "visibility": "public",
                "forks": 3415,
                "open_issues": 45,
                "watchers": 9004,
                "default_branch": "master",
                "score": 1.0
            }
        expected_keys = set([
            'repo_name',
            'repo_full_name',
            'owner',
            'owner_name',
            'owner_avatar_url',
            'owner_profile_url',
            'repo_description',
            'repo_url',
            'repo_html_url',
            'starts',
            'language',
            'open_issues_count',
            'teams_url',
            'has_issues',
            'has_discussions',
            'has_wiki',
            'archived',
            'disabled',
            'allow_forking',
            'forks',
            'visibility', 'id'])
        # action
        serialized_repo_data = repository_serializer(inbound_data) 
        assert expected_keys == serialized_repo_data.keys()

    def test_issue_serializer(self):
        """
        Test Issue Serializer
        """
        inbound_data = {
         "url":"https://api.github.com/repos/batterseapower/pinyin-toolkit/issues/132",
         "repository_url":"https://api.github.com/repos/batterseapower/pinyin-toolkit",
         "labels_url":"https://api.github.com/repos/batterseapower/pinyin-toolkit/issues/132/labels{/name}",
         "comments_url":"https://api.github.com/repos/batterseapower/pinyin-toolkit/issues/132/comments",
         "events_url":"https://api.github.com/repos/batterseapower/pinyin-toolkit/issues/132/events",
         "html_url":"https://github.com/batterseapower/pinyin-toolkit/issues/132",
         "id":35802,
         "node_id":"MDU6SXNzdWUzNTgwMg==",
         "number":132,
         "title":"Line Number Indexes Beyond 20 Not Displayed",
         "user":{
            "login":"Nick3C",
            "id":90254,
            "node_id":"MDQ6VXNlcjkwMjU0",
            "avatar_url":"https://secure.gravatar.com/avatar/934442aadfe3b2f4630510de416c5718?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png",
            "gravatar_id":"",
            "url":"https://api.github.com/users/Nick3C",
            "html_url":"https://github.com/Nick3C",
            "followers_url":"https://api.github.com/users/Nick3C/followers",
            "following_url":"https://api.github.com/users/Nick3C/following{/other_user}",
            "gists_url":"https://api.github.com/users/Nick3C/gists{/gist_id}",
            "starred_url":"https://api.github.com/users/Nick3C/starred{/owner}{/repo}",
            "subscriptions_url":"https://api.github.com/users/Nick3C/subscriptions",
            "organizations_url":"https://api.github.com/users/Nick3C/orgs",
            "repos_url":"https://api.github.com/users/Nick3C/repos",
            "events_url":"https://api.github.com/users/Nick3C/events{/privacy}",
            "received_events_url":"https://api.github.com/users/Nick3C/received_events",
            "type":"User",
            "site_admin":True
         },
         "labels":[
            {
               "id":4,
               "node_id":"MDU6TGFiZWw0",
               "url":"https://api.github.com/repos/batterseapower/pinyin-toolkit/labels/bug",
               "name":"bug",
               "color":"ff0000"
            }
         ],
         "state":"open",
         "assignee":None,
         "milestone":{
            "url":"https://api.github.com/repos/octocat/Hello-World/milestones/1",
            "html_url":"https://github.com/octocat/Hello-World/milestones/v1.0",
            "labels_url":"https://api.github.com/repos/octocat/Hello-World/milestones/1/labels",
            "id":1002604,
            "node_id":"MDk6TWlsZXN0b25lMTAwMjYwNA==",
            "number":1,
            "state":"open",
            "title":"v1.0",
            "description":"Tracking milestone for version 1.0",
            "creator":{
               "login":"octocat",
               "id":1,
               "node_id":"MDQ6VXNlcjE=",
               "avatar_url":"https://github.com/images/error/octocat_happy.gif",
               "gravatar_id":"",
               "url":"https://api.github.com/users/octocat",
               "html_url":"https://github.com/octocat",
               "followers_url":"https://api.github.com/users/octocat/followers",
               "following_url":"https://api.github.com/users/octocat/following{/other_user}",
               "gists_url":"https://api.github.com/users/octocat/gists{/gist_id}",
               "starred_url":"https://api.github.com/users/octocat/starred{/owner}{/repo}",
               "subscriptions_url":"https://api.github.com/users/octocat/subscriptions",
               "organizations_url":"https://api.github.com/users/octocat/orgs",
               "repos_url":"https://api.github.com/users/octocat/repos",
               "events_url":"https://api.github.com/users/octocat/events{/privacy}",
               "received_events_url":"https://api.github.com/users/octocat/received_events",
               "type":"User",
               "site_admin":False
            },
            "open_issues":4,
            "closed_issues":8,
            "created_at":"2011-04-10T20:09:31Z",
            "updated_at":"2014-03-03T18:58:10Z",
            "closed_at":"2013-02-12T13:22:01Z",
            "due_on":"2012-10-09T23:39:01Z"
         },
         "comments":15,
         "created_at":"2009-07-12T20:10:41Z",
         "updated_at":"2009-07-19T09:23:43Z",
         "closed_at": None,
         "pull_request":{
            "url":"https://api/github.com/repos/octocat/Hello-World/pull/1347",
            "html_url":"https://github.com/octocat/Hello-World/pull/1347",
            "diff_url":"https://github.com/octocat/Hello-World/pull/1347.diff",
            "patch_url":"https://api.github.com/repos/octocat/Hello-World/pulls/1347"
         },
         "body":"...",
         "score":1,
         "locked":True,
         "author_association":"COLLABORATOR",
         "state_reason":"completed"
      }

        expected_keys = set([
            'issue_url',
            'issue_title',
            'issue_html_url',
            'repository_url',
            'comments',
            'comments_url',
            'state',
            'created_at',
            'closed_at',
            'updated_at',
            'locked',
            'body',
            'assignee',
            'id'
        ])
        # action 
        serialized_data = issue_serializer(inbound_data)

        assert expected_keys == serialized_data.keys()