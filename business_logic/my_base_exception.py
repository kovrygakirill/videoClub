from django.http import JsonResponse
from django.conf import settings
import functools
import traceback


def base_view(function):
    @functools.wraps(function)
    def inner(request, *args, **kwargs):
        try:
            return function(request, *args, **kwargs)
        except Exception as ex:
            return error_response(ex)

    return inner


def error_response(exception):
    trback = ""
    if settings.DEBUG:
        trback = traceback.format_exc()

    return JsonResponse(
        {
            "error_Message": str(exception),
            "traceback": trback
        },
        status=400,
        safe=not isinstance(exception, list),
    )
