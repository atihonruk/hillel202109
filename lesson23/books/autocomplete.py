from django_redis import get_redis_connection

'books:book:title'


def make_key(model, field_name):
    return ':'.join([model.__module__, model.__name__, field_name])


# 'AnotherBook:2', 'Book:1'

SEPARATOR = ':'


def field_completions(obj, field_name):
    #     book. 'title'
    val = obj.__dict__[field_name]
    if val:
        val = val.lower()
        # TODO: make more completions
    return [val]


def model_completions(model, field_name):
    key = make_key(model, field_name)

    # Get objects from DB
    completions = []
    for obj in model.objects.all():
        for compl in field_completions(obj, field_name):
            completions.append(SEPARATOR.join((compl, str(obj.id))))

    con = get_redis_connection()
    con.zremrangebyrank(key, 0, -1)
    con.zadd(key, {k:0.0 for k in completions})
    return completions


def get_completions(model, field, prefix, min_length=0):
    
    if prefix and len(prefix) > min_length:
        con = get_redis_connection()
        # ZRANGEBYLEX key min max
        prefix = '[' + prefix # [a
        min_ = prefix.encode('utf-8')
        max_ = min_ + b'\xff'
        key = make_key(model, field)
        id_list = con.zrangebylex(key, min_, max_)
        return [val.decode('utf-8').split(':') for val in id_list]
