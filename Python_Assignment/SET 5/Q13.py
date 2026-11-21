class AppError(Exception):
    def __init__(self, msg="app failed", *, code=1):
        super().__init__(msg)
        self.code = code


class DbError(AppError):
    def __init__(self, table, **kw):
        super().__init__(f"db error in {table}", **kw)
        self.table = table


class NotFound(DbError, KeyError):
    pass


def fetch(t):
    if t == "x":
        raise NotFound("x", code=404)

    if t == "y":
        raise DbError("y")

    if t == "z":
        raise AppError()

    raise KeyError(t)


for t in "xyzw":
    try:
        fetch(t)
    except NotFound as e:
        print("NotFound", e, e.code, e.args)
    except DbError as e:
        print("DbError", e, e.code)
    except (KeyError, AppError) as e:
        print(type(e).__name__, e)


print([c.__name__ for c in NotFound.__mro__])
print(str(KeyError("k")), issubclass(NotFound, LookupError))


#OUTPUT
NotFound 'db error in x' 404 ('db error in x',)
DbError db error in y 1
AppError app failed
KeyError 'w'
['NotFound', 'DbError', 'AppError', 'KeyError', 'LookupError', 'Exception', 'BaseException', 'object']
'k' True

Process finished with exit code 0