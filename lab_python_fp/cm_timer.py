import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.perf_counter()

    def __exit__(self, exp_type, exp_value, traceback):
        print(f'time: {time.perf_counter() - self.start_time}')


@contextmanager
def cm_timer_2():
    start_time = time.perf_counter()
    yield
    print(f'time: {time.perf_counter() - start_time}')


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(1)
    with cm_timer_2():
        time.sleep(1)
