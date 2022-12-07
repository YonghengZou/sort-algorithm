from select_sort import Select
from bubble_sort import Bubble
from insertion_sort import Insertion
from merge_sort import Merge
import random
import time
import matplotlib.pyplot as plt

def time_complexity(n, f):
    time_list = []
    for i in range(1, n, 50):
        nums = random.sample(range(1, 100001), i)
        start = time.time()
        # Sort.selection_sort(nums)
        f(nums)
        end = time.time()
        duration = end - start
        time_list.append(duration)
    return time_list
    
if "__main__"==__name__:
    x = random.sample(range(1, 100), 15)
    print(x)
    result = Merge.sort(x, reverse=True)
    print(result)
    plt.plot(time_complexity(2000, Select.sort), label='select sort')
    plt.plot(time_complexity(2000, Bubble.sort), label='bubble sort')
    plt.plot(time_complexity(2000, Insertion.sort), label='Insertion sort')
    plt.plot(time_complexity(2000, Merge.sort), label='Merge sort')
    plt.legend()
    plt.show()
