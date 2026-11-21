import threading
import queue


lock = threading.Lock()
rlock = threading.RLock()


def try_nested(l):
    with l:
        got = l.acquire(blocking=False)

        if got:
            l.release()

        return got


print(try_nested(lock), try_nested(rlock))


results = {}
q = queue.Queue()


def worker(tid):
    while True:
        item = q.get()

        if item is None:
            q.task_done()
            break

        results[item] = item * item
        q.task_done()


threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]

for t in threads:
    t.start()

for n in range(6):
    q.put(n)

q.join()

for _ in threads:
    q.put(None)

for t in threads:
    t.join()

print(sorted(results.items()))
print(len(results), [t.is_alive() for t in threads])


event = threading.Event()
out = []


def waiter():
    out.append(event.wait(timeout=5))


t = threading.Thread(target=waiter)
t.start()

event.set()
t.join()

print(out, threading.active_count())
#SOLUTION
False True
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
6 [False, False, False]
[True] 1

Process finished with exit code 0