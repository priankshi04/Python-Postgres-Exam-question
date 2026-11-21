import functools
import io
import logging

stream = io.StringIO()
handler = logging.StreamHandler(stream)
handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s:%(message)s"))

svc = logging.getLogger("svc")
svc.addHandler(handler)
svc.setLevel(logging.INFO)
svc.propagate = False


def traced(level):
    def deco(fn):
        log = logging.getLogger(f"svc.{fn.__name__}")

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            log.log(level, "enter %s", args)

            try:
                result = fn(*args, **kwargs)
            except Exception:
                log.exception("boom")
                raise

            log.log(level, "exit %s", result)
            return result

        return wrapper

    return deco


@traced(logging.DEBUG)
def quiet(x):
    return x + 1


@traced(logging.INFO)
@traced(logging.WARNING)
def loud(x):
    return 10 / x


quiet(1)
loud(2)

try:
    loud(0)
except ZeroDivisionError:
    print("caught")

for line in stream.getvalue().splitlines():
    if line.split(":")[0] in ("DEBUG", "INFO", "WARNING", "ERROR"):
        print(line)

OUTPUT
caught
INFO:svc.loud:enter (2,)
WARNING:svc.loud:enter (2,)
WARNING:svc.loud:exit 5.0
INFO:svc.loud:exit 5.0
INFO:svc.loud:enter (0,)
WARNING:svc.loud:enter (0,)
ERROR:svc.loud:boom
ERROR:svc.loud:boom

Process finished with exit code 0