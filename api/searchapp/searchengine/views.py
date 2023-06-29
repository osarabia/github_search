from . import Engine

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .cache import flush_everything
from .helpers import error_to_http, sanitize_search_criteria


@api_view(['POST'])
def search_view(request):
    """
    Search View
    """
    search_criteria = request.data.get('search_criteria', '')
    search_criteria = sanitize_search_criteria(search_criteria)
    entity_type = request.data.get('entity_type', '')
    print(search_criteria, entity_type)
    if len(search_criteria) == 0 or len(entity_type) == 0:
        return Response(data="", status=400)

    search_engine = Engine()
    error, data = search_engine.search(search_criteria, entity_type)
    if len(error) > 0:
        response_code = error_to_http(error)
        if response_code:
            return Response(data="", status=response_code)

    return Response(data)


@api_view(['GET'])
def clear_cache(request):
    """
    Clean Cache
    """
    flush_everything()
    return Response(data="", status=200)