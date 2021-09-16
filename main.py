import queue

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
                best.put((-item, -n, line))
                max_time = -best.queue[0][0]
        else:
            best.put((-item, -n, line))
            max_time = -best.queue[0][0]

    while not best.empty():
        print(best.get()[2].strip())
