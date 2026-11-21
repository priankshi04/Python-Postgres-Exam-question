import contextlib
import threading


def run(use_lock):
    state = {"counter": 0}
    lock = threading.Lock() if use_lock else contextlib.nullcontext()

    a_read, b_done = threading.Event(), threading.Event()
    waited = []

    def thread_a():
        with lock:
            tmp = state["counter"]
            a_read.set()
            waited.append(b_done.wait(timeout=0.3))
            state["counter"] = tmp + 1

    def thread_b():
        a_read.wait()

        with lock:
            state["counter"] += 1

        b_done.set()

    ts = [
        threading.Thread(target=thread_a),
        threading.Thread(target=thread_b)
    ]

    for t in ts:
        t.start()

    for t in ts:
        t.join()

    return state["counter"], waited[0], b_done.is_set()


print(run(False))
print(run(True))


#OUTPUT
(1, True, True)
(2, False, True)

Process finished with exit code 0