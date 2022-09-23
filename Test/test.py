import psutil
while True:
    print(psutil.net_io_counters().bytes_recv)
    (float(psutil.cpu_freq().min))







