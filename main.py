import queue
import time

t1 = time.time()
top_size = 10
max_time = float('inf')

with open('ratings.csv', 'r') as f:
    best = queue.PriorityQueue(maxsize=10)
    i = 0
    for n, line in enumerate(f):
        if n == 0:
            i = line.strip().split(',').index("timestamp")
            continue
        item = int(line.split(',')[i])
        if n > top_size:
            if item < max_time:
                best.get()
                best.put(-item)
                max_time = -best.queue[0]
        else:
            best.put(-item)
            max_time = -best.queue[0]

    for i in range(top_size):
        print(-best.get())
t2 = time.time()
print(f"Time: {t2-t1}")
