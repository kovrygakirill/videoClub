from urllib.parse import urlencode
from django.http.request import QueryDict


class PathRequest:
    @staticmethod
    def getQueryWithoutPage(path_url):
        if path_url:
            query_as_dict = QueryDict(path_url).copy()
            if query_as_dict.get('page'):
                del query_as_dict['page']
            query_as_string = urlencode(query_as_dict)
            if query_as_string:
                query_as_string += "&"

            return query_as_string
        else:
            return ''

    # @staticmethod
    # def getPathQuery(oldPath, newQuery):
    #     if oldPath:
    #         oldPath_dict = QueryDict(oldPath).copy()
    #         newQuery_dict = QueryDict(newQuery).copy()
    #
    #         if oldPath_dict.keys() & newQuery_dict.keys():
    #             replayKey = (oldPath_dict.keys() & newQuery_dict.keys()).pop()
    #             oldPath_dict[replayKey] = newQuery_dict[replayKey]
    #
    #             newPath = urlencode(oldPath_dict)
    #         else:
    #             newPath = oldPath + "&" + newQuery
    #
    #         return newPath
    #     else:
    #         return newQuery
