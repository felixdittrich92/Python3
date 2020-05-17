# wenig sinnvoll - läuft nicht parallel

import time
import math

from threading import Thread

NUM_THREADS = 4

def calc(num_elements):
    res = 0
    for i in range(num_elements):
        res += math.sqrt(i)
    print(res)

def main():
    threads = []
    for _ in range(NUM_THREADS):
        threads.append(Thread(target=calc, args=[8_000_000])) # Aufgabe übergeben

    start_time = time.perf_counter()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()  # warten bis alle Threads fertig sind 

    end_time = time.perf_counter()
    print("Took: {} s".format(end_time - start_time))

if __name__ == "__main__":
    main()