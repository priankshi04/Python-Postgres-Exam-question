import multiprocessing as mp
import os
import threading


config = {"factor": 2}


def scale(x):
    return x * config["factor"]


def inverse(x):
    return 1 / x


def pid(_):
    return os.getpid()


def init_worker(f):
    config["factor"] = f


if __name__ == "__main__":
    ctx = mp.get_context("spawn")

    with ctx.Pool(2, initializer=init_worker, initargs=(5,)) as pool:
        print(pool.map(scale, range(5)))
        print(pool.apply_async(scale, (3,)).get())

        try:
            pool.map(inverse, [1, 0, 2])
        except ZeroDivisionError as e:
            print("ZeroDivisionError:", e)

        print(1 <= len(set(pool.map(pid, range(8)))) <= 2)

    print(config["factor"])

    t = threading.Thread(target=lambda: config.update(factor=9))
    t.start()
    t.join()

    print(config["factor"])

 OUTPUT
[0, 5, 10, 15, 20]
15
ZeroDivisionError: division by zero
True
2
9

Process finished with exit code 0
