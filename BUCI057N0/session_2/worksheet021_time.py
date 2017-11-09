import time

total_seconds = time.time()

d = int(total_seconds / 3600 / 24)

h = int((total_seconds - d*3600*24) / 3600)
m = int(h - int((total_seconds - d*3600*24) / 3600) / 24)
s = int(total_seconds - (d * 3600 * 24) - (h * 3600) - (m * 60))

print('{} {}:{}:{}'.format(d, h, m, s))
