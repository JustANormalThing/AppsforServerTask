import threading
import time

counter = 0
lock = threading.RLock()  
ITERATIONS = 100_000

class IncrementThread(threading.Thread):
    def run(self):
        global counter
        for _ in range(ITERATIONS):
            with lock:
                counter += 1

class DecrementThread(threading.Thread):
    def run(self):
        global counter
        for _ in range(ITERATIONS):
            with lock:
                counter -= 1

def main(n, m):
    global counter
    counter = 0
    threads = []

    start_time = time.time()

    for _ in range(n):
        t = IncrementThread()
        threads.append(t)
        t.start()

    for _ in range(m):
        t = DecrementThread()
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()

    print(f"Final counter value: {counter}")
    print(f"Time elapsed: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    main(n, m)