import platform
import time
import psutil
import cpuinfo
import GPUtil 

from tqdm import tqdm
from time import sleep
import psutil
import socket


hostname= socket.gethostname()


Ip = socket.gethostbyname(hostname)
my_cpuinfo = cpuinfo.get_cpu_info()
gpus = GPUtil.getGPUs()
gpu_name = None
gpu_load = None
gpu_mem_free = None
gpu_mem_used = None
gpu_mem_total = None
gpu_temp = None
if gpus:
    gpu = gpus[0]
    gpu_name = gpu.name
    gpu_load = f"{gpu.load*100}%"
    gpu_mem_free = f"{gpu.memoryFree}MB"
    gpu_mem_used = f"{gpu.memoryUsed}MB"
    gpu_mem_total = f"{gpu.memoryTotal}MB"
    gpu_temp = f"{gpu.temperature} °C"

print(f"""
/  _ \/ ___\               OS : {platform.system()} {platform.node()} 
| / \||    \               DEVICE : {platform.machine()} 
| \_/|\___ |               CPU: {my_cpuinfo['brand_raw'] }
\____/\____/               CPU SPEED:{my_cpuinfo['hz_actual_friendly'] }
                           IP:{Ip}
                           GPU:{gpu_name}
""" )

with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
    while True:
        rambar.n=psutil.virtual_memory().percent
        cpubar.n=psutil.cpu_percent()
        rambar.refresh()
        cpubar.refresh()
        sleep(1)