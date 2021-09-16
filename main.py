import queue
import time
t1 = time.time()
with open('ratings.csv', 'r') as f:
    best = queue.PriorityQueue(maxsize=11)
    i = 0
    for n, line in enumerate(f):
        if n == 0:
            i = line.split(',').index("timestamp\n")
            continue
        best.put(-int(line.split(',')[i]))
        if n > 10:
            best.get()

    for i in range(10):
        print(-best.get())
t2 = time.time()
print(f"Time: {t2-t1}")
#
# bufsize = 65536
# with open(path) as infile:
#     while True:
#         lines = infile.readlines(bufsize)
#         if not lines:
#             break
#         for line in lines:
#             process(line)
