
from .fetcher import Fetcher
from typing import List, Dict, Tuple


class Engine:
    """
    Search Engine Entry Point Class
    """
    def __init__(self):
        self.fetcher = Fetcher()

    def search(self, search_criteria: str,
               entity_type: str) -> Tuple[str, List[Dict]]:
        """
        Search Functionality Starts Here
        """
        return self.fetcher.fetch(search_criteria, entity_type)