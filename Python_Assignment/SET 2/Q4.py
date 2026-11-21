import functools
import logging

records = []


class ListHandler(logging.Handler):
    def emit(self, record):
        records.append((record.levelname, record.getMessage(),
                        record.exc_info is not None, record.funcName))


log = logging.getLogger("audit")
log.setLevel(logging.DEBUG)
log.addHandler(ListHandler())
log.propagate = False


def audited(level=logging.INFO):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            log.log(level, "call %s%r", fn.__name__, args)
            try:
                result = fn(*args, **kwargs)
            except ZeroDivisionError:
                log.exception("failed %s", fn.__name__)
                return None
            else:
                log.debug("ok %s -> %r", fn.__name__, result)
                return result
            finally:
                log.log(logging.DEBUG, "done")

        return wrapper
    return deco


@audited()
def div(a, b):
    return a / b


@audited(logging.WARNING)
def neg(a):
    return -a


print(div(6, 3), div(1, 0), neg(4))

for r in records:
    print(r)
#SOLUTION
2.0 None -4
('INFO', 'call div(6, 3)', False, 'wrapper')
('DEBUG', 'ok div -> 2.0', False, 'wrapper')
('DEBUG', 'done', False, 'wrapper')
('INFO', 'call div(1, 0)', False, 'wrapper')
('ERROR', 'failed div', True, 'wrapper')
('DEBUG', 'done', False, 'wrapper')
('WARNING', 'call neg(4,)', False, 'wrapper')
('DEBUG', 'ok neg -> -4', False, 'wrapper')
('DEBUG', 'done', False, 'wrapper')

Process finished with exit code 0
