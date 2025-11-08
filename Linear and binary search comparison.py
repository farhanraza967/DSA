import time
import matplotlib.pyplot as plt

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def binary_search(data, target):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

sizes = []
linear_best = []
linear_worst = []
binary_best = []
binary_worst = []

for size in range(10000, 2000000, 50000):
    data = list(range(size))
    sizes.append(len(data))

    t1 = time.time()
    linear_search(data, 0)
    t2 = time.time()
    linear_best.append(t2 - t1)

    t1 = time.time()
    linear_search(data, -1)
    t2 = time.time()
    linear_worst.append(t2 - t1)

    t1 = time.time()
    binary_search(data, data[len(data)//2])
    t2 = time.time()
    binary_best.append(t2 - t1)

    t1 = time.time()
    binary_search(data, -1)
    t2 = time.time()
    binary_worst.append(t2 - t1)

plt.figure(figsize=(5.5, 3.8))
plt.plot(sizes, linear_best, color='blue', label='Linear Best Case')
plt.plot(sizes, binary_best, color='green', label='Binary Best Case')
plt.title('Comparison of Best Case: Linear vs Binary Search')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()


plt.figure(figsize=(5.5, 3.8))
plt.plot(sizes, linear_worst, color='red', label='Linear Worst Case')
plt.plot(sizes, binary_worst, color='orange', label='Binary Worst Case')
plt.title('Comparison of Worst Case: Linear vs Binary Search')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
