import subprocess
import platform
import socket

def getSize(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    hours = int(uptime_seconds // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    seconds = int(uptime_seconds % 60)
    return f"{hours}h {minutes}m {seconds}s"

def get_cpu_name():
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if "model name" in line:
                    cpu = line.strip().split(":")[1].strip()
                    return cpu if len(cpu) <= 45 else cpu[:42] + "..."
    except:
        return platform.processor()

def get_gpu_name():
    try:
        output = subprocess.check_output(
            "lspci | grep -i 'vga\\|3d\\|2d'", shell=True, text=True
        )
        gpu = output.split(":")[2].strip()
        return gpu
    except:
        return "No GPU Found"

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "N/A"