from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):

    print(f"----------{request.GET=}")
    print(f"----------{request.POST=}")

    data = {}
    try:
        data = json.loads(request.body)
    except Exception:
        pass

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data["content_type"] = request.content_type

    return JsonResponse(data)
