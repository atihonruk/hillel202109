from datetime import datetime
from importlib import import_module
from django.urls import path
from django.http import HttpResponse, HttpResponseNotFound
from django.core.cache import cache

from django_redis import get_redis_connection

def rate_limit(get_response):

    def limit_request(request):
        remote_ip = request.META['REMOTE_ADDR']
        minute = datetime.now().minute
        key = f'rate_limit:{remote_ip}:{minute}'
        con = get_redis_connection()

        hits = 0
        try:
            with con.pipeline() as pipe:
                pipe.multi() # begin
                pipe.incr(key)
                pipe.expire(key, 60)
                hits, _ = pipe.execute()
        except Exception as e:
            print(e)

        if hits > RATE_LIMIT:
            return HttpResponse(f'Too many requests from {remote_ip}', status=429)
        else:
            return get_response(request)

    return limit_request


RATE_LIMIT = 5
DEBUG=True
ROOT_URLCONF=__name__
SECRET_KEY='soo secret'
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379'
    }
}
MIDDLEWARE = [
    'doc.rate_limit',
]


def mod_handler(request, mod_name):
    try:
        mod = import_module(mod_name)
        names = [name for name in dir(mod) if not name.startswith('_')]
        ...
        return HttpResponse() # render
    except ImportError as e:
        return HttpResponseNotFound(e)


def obj_handler(request, mod_name, obj_name):
    hits = cache.get(request.path_info, -1)
    if hits == -1:
        cache.set(request.path_info, 0)

    cache.incr(request.path_info)
    try:
        mod = import_module(mod_name)
        obj = getattr(mod, obj_name)

        return HttpResponse(f'{hits}\n\n' + obj.__doc__, content_type='text/plain')
    except (ImportError, AttributeError) as e:
        return HttpResponseNotFound(e)


urlpatterns = [
    path('<mod_name>', mod_handler),
    path('<mod_name>/<obj_name>', obj_handler),
]


if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line()
