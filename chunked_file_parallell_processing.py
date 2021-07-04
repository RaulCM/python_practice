import fileinput
import copy
import logging
import time
from queue import Queue
from threading import Thread



format = "%(asctime)s.%(msecs)03d %(threadName)s %(levelname)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")

def process(batch):
    # TODO define the actual processing
    logging.info(f"Start Batch {batch}")
    time.sleep(5)
    logging.info(f"Processed Batch {batch}")


def worker(task_queue):
    """
    This is executed in the worker threads, which processes items in the queue one after another.
    These daemon threads go into an infinite loop, and only exit when the main thread ends.
    """
    while True:
        logging.info('Polling next task')
        batch = task_queue.get(block=True)
        process(batch)
        batch.clear()
        task_queue.task_done()


def submit(batch, task_queue):
    # block till more space available
    task_queue.put(copy.deepcopy(batch), block=True)
    logging.info(f"Submitted Batch {batch}")
    batch.clear()


parallelism = 3
chunks_to_buffer = 1 # pool extra chunks when all workers are busy
task_queue = Queue(maxsize=chunks_to_buffer)
# Set up daemons to process the tasks
for i in range(parallelism):
    Thread(target=worker, args=(task_queue,), daemon=True).start()


batch = []
batch_size = 7

with fileinput.input(files=('data1.csv', 'data2.csv')) as f:
    for line in f:
        batch.append(line.strip())
        if len(batch) == batch_size:
            submit(batch, task_queue)

if len(batch) > 0:
    submit(batch, task_queue)


logging.info('Waiting for all Tasks to complete')
task_queue.join()
logging.info('All tasks done')
