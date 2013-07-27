#!/usr/bin/env python3

from easypool2 import ThreadPool
from threading import RLock
import random
import time
from collections import deque
from collections import OrderedDict

hi_str = '1234'
hi_list = [1, 2, 3, 4]
hi_set = set(hi_list)
hi_deque = deque(hi_list)
hi_float = 4.444
hi_int = 4
hi_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
hi_bool = True 

variable_types_list = [hi_str, hi_list, hi_set, hi_deque, hi_float, hi_int, hi_dict, hi_bool]

#variable_types_list = [hi_dict]

# my_pool = ThreadPool(my_float, send_item=True)
threadlock = RLock()

def print_hi(x):
    sleep = random.randint(0,4)
    sleep = 1
    time.sleep(sleep)
    threadlock.acquire()
    #print("hi_dict key %s has a value of %s" % (x, hi_dict[x]))
    print("Function Value: %s says 'Hi!' after sleeping %s seconds" % (x, sleep))
    threadlock.release()
    return

for variable_type in variable_types_list:
    my_pool = ThreadPool(variable_type, send_item=False, max_pool=50, min_pool=80)
    print("Total pool size: %s" % my_pool.pool_size)
    print(str(type(variable_type)) + " test for send_item=False")
    print("Variable values: %s" % variable_type)
    for i in list(range(100)):
        i += 1
        my_pool.add_task(print_hi, i)
        time.sleep(0.1)
    my_pool.wait_completion()
    print("")
    my_pool = ThreadPool(variable_type, send_item=True, max_pool=50, min_pool=80)
    print("Total pool size: %s" % my_pool.pool_size)
    print(str(type(variable_type)) + " test for send_item=True")
    print("Variable values: %s" % variable_type)
    for i in list(range(100)):
        i += 1
        my_pool.add_task(print_hi)
        time.sleep(0.1)
    my_pool.wait_completion()
    print("")

#for variable_type in variable_types_list:
#    my_pool = ThreadPool(variable_type, send_item=True)
#    print str(type(variable_type)) + " test for send_item=True"
#    print "Variable values: %s" % variable_type
#    for i in xrange(5):
#        my_pool.add_task(print_hi)
#    my_pool.wait_completion()
#    print ""

#my_pool.wait_completion()
