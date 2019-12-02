from urllib.parse import urlencode
from django.http.request import QueryDict


class PathRequest:
    @staticmethod
    def sumQuery(path_url):
        if path_url:
            query_as_dict = QueryDict(path_url).copy()
            if query_as_dict.get('page'):
                del query_as_dict['page']
            query_as_string = urlencode(query_as_dict)
            query_as_string += "&"

            return query_as_string
        else:
            return ''
