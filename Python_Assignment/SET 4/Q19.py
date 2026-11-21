import threading


lock_a, lock_b = threading.Lock(), threading.Lock()
barrier = threading.Barrier(2)
result = {}


def worker(name, first, second):
    with first:
        barrier.wait()
        got = second.acquire(timeout=0.3)
        result[name] = got
        barrier.wait()

        if got:
            second.release()


t1 = threading.Thread(target=worker, args=("t1", lock_a, lock_b))
t2 = threading.Thread(target=worker, args=("t2", lock_b, lock_a))

t1.start()
t2.start()
t1.join()
t2.join()

print(sorted(result.items()))
print(lock_a.locked(), lock_b.locked())


local = threading.local()
seen = []


def show(v):
    local.v = v
    seen.append((v, local.v))


ts = [threading.Thread(target=show, args=(i,)) for i in range(3)]

for t in ts:
    t.start()

for t in ts:
    t.join()

local.v = "main"

print(sorted(seen), local.v, hasattr(local, "missing"))


sem = threading.Semaphore(2)
active, peak, guard = [], [0], threading.Lock()


def limited():
    with sem:
        with guard:
            active.append(1)
            peak[0] = max(peak[0], len(active))

        with guard:
            active.pop()


threads = [threading.Thread(target=limited) for _ in range(6)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(1 <= peak[0] <= 2, len(active))

OUTPUT
[('t1', False), ('t2', False)]
False False
[(0, 0), (1, 1), (2, 2)] main False
True 0

Process finished with exit code 0