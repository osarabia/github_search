import logging
import requests
from typing import List, Tuple
from json import JSONDecodeError
from .serializers import serialize


ENTITY_TYPE_FROM_API_URL = {
    "users": "https://api.github.com/search/users?q=",
    "repositories": "https://api.github.com/search/repositories?q=",
    "issues": "https://api.github.com/search/issues?q="
}


class GithubApi:
    """
    Interaction GitHub API
    """

    def validate_response(self, resp) -> Tuple[str, List]:
        """
        Validate http response
        """
        error, content = "", []
        try:
            content = resp.json()
            if 'items' not in content:
                error = "rest_api_unexpected_output"
                logging.error(error)
                return error, content
        except JSONDecodeError as json_error:
            error = f"rest_api_unable_to_decode_json_response|{json_error}"
            logging.error(error)
            return error, content

        return error, content['items']

    def serialize_response(self, resp, entity_type) -> Tuple[str, List]:
        """
        Serialize Github Api Response
        """
        error, content = self.validate_response(resp)
        try:
            serialized_data = [serialize(entity_type, item)
                               for item in content] 

        except Exception as exception:
            error = f"rest_api_unable_to_serialize_response|{exception}"
            logging.error(error)
            return error, []

        return error, serialized_data

    def do_request(self, search_criteria, entity_type) -> Tuple[str, List]:
        """Perform http request"""
        error, result = "", []
        url = ENTITY_TYPE_FROM_API_URL.get(entity_type, '')
        if len(url) == 0:
            error = "rest_api_wrong_entity"
            logging.error(error)
            return error, result

        url = f"{url}{search_criteria}"

        try:
            resp = requests.get(url, timeout=5)
        except requests.exceptions.Timeout:
            error = "rest_api_timeout"
            logging.error(error)
            return error, result
        if resp.status_code != 200:
            error = f"resp_api_not_ok|{resp.status_code}"
            logging.error(error)
            return error, result

        return self.serialize_response(resp, entity_type)
