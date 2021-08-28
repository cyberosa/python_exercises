# Merging two sorted lists using different methods
from heapq import merge
import tracemalloc
import random
import time

# Generate lists
def generate_random_list():
    list1 = list()
    for i in range(30000):
        n = random.randint(1, 4000)
        list1.append(n)
    return list1


list_1 = sorted(generate_random_list())
list_2 = sorted(generate_random_list())

# Method 1
tracemalloc.start()
start = time.time()
size_1 = len(list_1)
size_2 = len(list_2)

res = []
i, j = 0, 0

while i < size_1 and j < size_2:
    if list_1[i] < list_2[j]:
        res.append(list_1[i])
        i += 1

    else:
        res.append(list_2[j])
        j += 1

res = res + list_1[i:] + list_2[j:]
current, peak = tracemalloc.get_traced_memory()
print(f"M1: Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
tracemalloc.stop()
end = time.time()
print("The M1 job ended in {}".format(end - start))

# Method 2
tracemalloc.start()
start = time.time()
res = sorted(list_1 + list_2)
current, peak = tracemalloc.get_traced_memory()
print(f"M2: Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
tracemalloc.stop()
end = time.time()
print("The M2 job ended in {}".format(end - start))

# Method 3
tracemalloc.start()
start = time.time()
# using heapq.merge()
# to combine two sorted lists
res = list(merge(list_1, list_2))
current, peak = tracemalloc.get_traced_memory()
print(f"M3: Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
tracemalloc.stop()
end = time.time()
print("The M3 job ended in {}".format(end - start))

# Method 4
tracemalloc.start()
start = time.time()
# to treat each sorted list as a stack
sorted_list =[]
while list_1 and list_2:
    if list_1[0] <  list_2[0]:
        sorted_list.append(list_1.pop(0))
    else:
        sorted_list.append(list_2.pop(0))
sorted_list += list_1
sorted_list += list_2
current, peak = tracemalloc.get_traced_memory()
print(f"M4: Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
tracemalloc.stop()
end = time.time()
print("The M4 job ended in {}".format(end - start))