import time
import threading
import signal
import queue
import atexit

# stop = threading.Event()

Stop = object()


def worker(queue):
    n = 0
    for n in range(5):
        # if stop:
        #    return
        task = queue.get()
        if task is Stop:
            print('Exiting')
            queue.put_nowait(task)
            return
        else:
            print('Got task {task}')
        
        print(f'Working {n}')
        time.sleep(1)
        n += 1


def on_interrupt(sig, *args):
    print(f'Caught {sig}', args)
    # stop.set()
    # queue.put_nowait(Stop)

def on_exit():
    print('Python exit')

    
if __name__ == '__main__':
    signal.signal(signal.SIGINT, on_interrupt)
    atexit.register(on_exit)

    queue = queue.Queue()
    queue.put_nowait('Some task')

    t = threading.Thread(target=worker, args=(queue,))
    t.start()
    time.sleep(5)
    queue.put_nowait(Stop)
    
    t.join()
