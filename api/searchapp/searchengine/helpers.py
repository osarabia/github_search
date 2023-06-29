from __future__ import annotations


def error_to_http(error_string: str) -> int | None:
    """Parse Some Error String to Http Codes"""

    if error_string.startswith('rest_api_wrong_entity'):
        return 400
    if error_string == "resp_api_not_ok|403":
        return 503

    return None

def sanitize_search_criteria(search_criteria) -> str:
    """
    sanitize user search criteria
    """
    search = search_criteria.split('&')
    return search[0]