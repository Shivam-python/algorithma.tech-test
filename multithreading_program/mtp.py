import random
import string
import os
import sys
from threading import Thread,active_count
from queue import Queue

def get_random_str():
    # function for returning random string value
    S = 10 
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    return ran

def task(x):
    # function for creating file and writing random value
    with open(os.path.join(sys.path[0],f'{x}.txt'),'w+') as file:
        ran_str = get_random_str()
        file.write(ran_str)
    file.close()
    return

class FileWorker(Thread):
    """
    Thread class for creating files
    """
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            rand_int = self.queue.get()
            try:
                task(rand_int)
            finally:
                self.queue.task_done()

def main():
    queue = Queue() # queue for adding tasks
    for x in range(5): # 6 threads will be created, 1 main thread and 5 worker threads.
        worker = FileWorker(queue)
        # for exiting main thread even if the workers are blocking
        worker.daemon = True
        worker.start()

    # getting different filename and putting in queue 
    x = len(os.listdir(sys.path[0]))
    for i in range(x,x+5):
        queue.put(item=i)
    print(active_count()) # printing active thread count
    queue.join()


if __name__ == '__main__':
    main()