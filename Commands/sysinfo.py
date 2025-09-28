import psutil
import platform
import socket
import shutil
from Core.utils import getSize, get_uptime, get_cpu_name, get_gpu_name, get_ip

def get_sysinfo():
    uname = platform.uname()
    os_name = uname.system
    kernel = uname.release
    hostname = socket.gethostname()
    uptime = get_uptime()

    cpu_name = get_cpu_name()
    cores = psutil.cpu_count(logical=True)
    threads = psutil.cpu_count(logical=False)

    gpu_name = get_gpu_name()

    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    ram_used = getSize(mem.used)
    ram_total = getSize(mem.total)
    swap_used = getSize(swap.used)
    swap_total = getSize(swap.total)

    total, used, free = shutil.disk_usage("/")
    disk_total = getSize(total)
    disk_used = getSize(used)
    disk_free = getSize(free)
    disk_percent = f"{(used/total)*100:.0f}%"

    ip_address = get_ip()

    return {
        "os": os_name,
        "kernel": kernel,
        "hostname": hostname,
        "uptime": uptime,
        "cpu": cpu_name,
        "cores": cores,
        "threads": threads,
        "gpu": gpu_name,
        "ram_used": ram_used,
        "ram_total": ram_total,
        "swap_used": swap_used,
        "swap_total": swap_total,
        "disk_used": disk_used,
        "disk_total": disk_total,
        "disk_free": disk_free,
        "disk_percent": disk_percent,
        "ip": ip_address,
    }

def get_dashboard(data):
    return f"""
🖥  Panoptic - System Information
────────────────────────────────────
OS        : {data['os']} ({data['kernel']})
Hostname  : {data['hostname']}
Uptime    : {data['uptime']}

CPU       : {data['cpu']} ({data['cores']} cores, {data['threads']} threads)
GPU       : {data['gpu']}

RAM       : {data['ram_used']} / {data['ram_total']}
Swap      : {data['swap_used']} / {data['swap_total']}
Disk      : {data['disk_used']} / {data['disk_total']} ({data['disk_percent']} used)
Free Disk : {data['disk_free']}

IP Addr   : {data['ip']}
────────────────────────────────────
"""