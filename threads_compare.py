import os
import random
import shutil
import string
import time
from multiprocessing.pool import ThreadPool

import requests


def fetch_pic(num_pic):
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    for _ in range(int(num_pic)):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)


class timer():
    def __init__(self, message, result_list):
        self.message = message
        self.result_list = result_list

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = (time.time() - self.start)
        self.result_list.append(elapsed_time)
        print(self.message.format(elapsed_time))


if __name__ == "__main__":
    MAX_THREAD_COUNT = 50
    DATA_SIZE = 500
    result_list = []
    for thread_count in range(2, MAX_THREAD_COUNT, 2):
        input_data = [DATA_SIZE // thread_count for _ in range(thread_count)]
        with timer(f"Threads: {thread_count} " + "Time {} sec", result_list):
            with ThreadPool(thread_count) as pool:
                pool.map(fetch_pic, input_data)
        shutil.rmtree('img')  # Clean "garbage" after download
        os.mkdir('img')  # create IMG for new queue
    print(f"Minimum time {min(result_list)}")
