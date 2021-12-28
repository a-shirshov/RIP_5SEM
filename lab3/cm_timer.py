import time
from contextlib import contextmanager


class CmTimer:

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exp_type, exp_value, traceback):
        self.end_time = time.time()
        print('time: {}'.format(self.end_time - self.start_time))


@contextmanager
def cm_timer():
    start_time = time.time()
    yield
    end_time = time.time()
    print('time: {}'.format(end_time - start_time))


if __name__ == '__main__':
    with CmTimer():
        time.sleep(1.0)

    with cm_timer():
        time.sleep(1.0)
