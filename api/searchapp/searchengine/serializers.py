
"""
Serializers
"""
from typing import Dict


def serialize(entity_type: str, data: Dict) -> Dict:
    """
    serialize function
    """
    if entity_type == 'users':
        return user_serializer(data)
    if entity_type == 'repositories':
        return repository_serializer(data)
    return issue_serializer(data)


def user_serializer(data: Dict) -> Dict:
    """
    User Serializer
    """

    return {
        'id': data['id'],
        'profile_picture': data.get('avatar_url', ''),
        'name': data.get('name', ''),
        'profile_url': data.get('url', ''),
        'profile_html_url': data.get('html_url', ''),
        'repos_url': data.get('repos_url', ''),
        'bio': data.get('bio', ''),
        'email': data.get('email', ''),
        'blog': data.get('blog', ''),
        'company': data.get('company', ''),
        'location': data.get('location', '')
    }


def repository_serializer(data: Dict) -> Dict:
    """
    Repository Serializer
    """
    return {
        'id': data['id'],
        'repo_name': data.get('name', ''),
        'repo_full_name': data.get('full_name', ''),
        'owner': data.get('owner', {}).get('login', ''),
        'owner_name': data.get('owner', {}).get('name', ''),
        'owner_avatar_url': data.get('owner', {}).get('avatar_url', ''),
        'owner_profile_url': data.get('owner', {}).get('url', ''),
        'repo_description': data.get('description', ''),
        'repo_url': data.get('url', ''),
        'repo_html_url': data.get('html_url', ''),
        'starts': data.get('watchers_count', ''),
        'language': data.get('language', ''),
        'open_issues_count': data.get('open_issues_count', ''),
        'teams_url': data.get('teams_url', ''),
        'has_issues': data.get('has_issues', ''),
        'has_discussions': data.get('has_discussions', ''),
        'has_wiki': data.get('has_wiki', ''),
        'archived': data.get('archived', ''),
        'disabled': data.get('disabled', ''),
        'allow_forking': data.get('allow_forking', ''),
        'forks': data.get('forks', ''),
        'visibility': data.get('visibility', '')
    }


def issue_serializer(data: Dict) -> Dict:
    """
    Issue Serializer
    """
    return {
        'id': data['id'],
        'issue_url': data.get('url', ''),
        'issue_title':  data.get('title', ''),
        'issue_html_url': data.get('html_url', ''),
        'repository_url': data.get('repository_url', ''),
        'comments': data.get('comments', ''),
        'comments_url': data.get('comments_url', ''),
        'state': data.get('state', ''),
        'created_at': data.get('created_at', ''),
        'closed_at': data.get('closed_at', ''),
        'updated_at': data.get('updated_at', ''),
        'locked': data.get('locked', ''),
        'body': data.get('body', ''),
        'assignee': data['assignee'].get('url', '') if data.get('assignee', None) else ''
    }
