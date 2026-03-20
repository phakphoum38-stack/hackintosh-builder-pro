import psutil
import platform

def scan():

    data = {}

    data["cpu"] = platform.processor()

    data["ram"] = psutil.virtual_memory().total

    data["disk"] = [d.device for d in psutil.disk_partitions()]

    return data
