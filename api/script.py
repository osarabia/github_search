import requests


def hit_to_check_rate_limit(input_text):
    """
    Just a function to check how rate limit looks like
    """
    for i in range(0, 200):
        search_criteria = f"{input_text}{i}"
        resp = requests.post("http://localhost:8000/api/search",json={
            "search_criteria": search_criteria,
            "entity_type": "users"
        }, timeout=10)
        print(resp.status_code)


if __name__ == "__main__":
    hit_to_check_rate_limit("omar")