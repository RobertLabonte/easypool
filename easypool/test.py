#!/usr/bin/env python

from easypool import ThreadPool
from threading import RLock
import random
import time
from collections import deque

# Test options
min_pool = 0  # Minimum threadpool size (0 is default)
max_pool = 0  # Maximum threadpool size (0 is default)
iterations = 6  # Number of calls to print_hi function placed in queue
min_sleep = 1  # Minimum sleep time for print_hi function
max_sleep = 3  # Maximum sleep time for print_hi function
serialize = False  # Delay start of threads to ensure sequential insertion
queue_type = 'fifo'  # fifo (First in first out (Default)), lifo (Last in first out)

# Test data structures
hi_str = '1234'
hi_tuple = (1, 2, 3, 4)
hi_list = [1, 2, 3, 4]
hi_set = set(hi_list)
hi_deque = deque(hi_list)
hi_float = 4.444
hi_int = 4
hi_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
hi_bool = True 

variable_types_list = [hi_str, hi_tuple, hi_list, hi_set, hi_deque, hi_float, hi_int, hi_dict, hi_bool]
threadlock = RLock()

def print_hi(x):
    sleep = random.randint(min_sleep,max_sleep)
    if serialize == True:
        sleep = 1
    time.sleep(sleep)
    threadlock.acquire()
    print("Function Value: %s says 'Hi!' after sleeping %s seconds" % (x, sleep))
    threadlock.release()
    return

for variable_type in variable_types_list:
    my_pool = ThreadPool(variable_type, send_item=False, max_pool=max_pool, min_pool=min_pool, queue_type=queue_type)
    print("Total pool size: %s" % my_pool.pool_size)
    print(str(type(variable_type)) + " test for send_item=False")
    print("Variable values: %s" % str(variable_type))
    for i in list(range(iterations)):
        i += 1
        my_pool.add_task(print_hi, i)
        if serialize == True:
            time.sleep(0.1)
    my_pool.wait_completion()
    print("")
    my_pool = ThreadPool(variable_type, send_item=True, max_pool=max_pool, min_pool=min_pool, queue_type=queue_type)
    print("Total pool size: %s" % my_pool.pool_size)
    print(str(type(variable_type)) + " test for send_item=True")
    print("Variable values: %s" % str(variable_type))
    for i in list(range(iterations)):
        i += 1
        my_pool.add_task(print_hi)
        if serialize == True:
            time.sleep(0.1)
    my_pool.wait_completion()
    print("")
