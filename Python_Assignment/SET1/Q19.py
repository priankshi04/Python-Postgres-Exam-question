import threading
import multiprocessing as mp


counter = 0
lock = threading.Lock()


def work_t(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1


def work_p(n):
    global counter
    for _ in range(n):
        counter += 1


if __name__ == "__main__":
    ts = [threading.Thread(target=work_t, args=(10000,)) for _ in range(4)]

    for t in ts:
        t.start()

    for t in ts:
        t.join()

    print("threads:", counter)

    counter = 0
    ps = [mp.Process(target=work_p, args=(10000,)) for _ in range(4)]

    for p in ps:
        p.start()

    for p in ps:
        p.join()

    print("processes:", counter)
    print([p.exitcode for p in ps])
#SOLUTION
threads: 40000
processes: 0
[0, 0, 0, 0]

Process finished with exit code 0
