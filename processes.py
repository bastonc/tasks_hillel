import random
import multiprocessing
#import multiprocess as multiprocess

from threads_compare import timer


def fill_data(n):
    lst = []
    while n > 0:
        n -= 1
        lst.append(random.randint(1, 100))
    # print(f"Full len list: {len(lst)}")  # if needed have control


if __name__ == "__main__":
    FILL_DATA_SIZE = 1_000_000
    WORKERS_MAX = 500
    result_list = []
    for workers in range(1, WORKERS_MAX):
        input_data = [FILL_DATA_SIZE // workers for _ in range(workers)]
        with timer(f"Process {workers} " + "{} sec", result_list):
            with multiprocessing.Pool(workers) as pool:
                pool.map(fill_data, input_data)



