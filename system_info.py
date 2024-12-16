import os
import psutil
from datetime import datetime


def collect_system_info():
    data = {
        "computer_name": os.getenv("COMPUTERNAME", "Unknown"),
        "user_name": os.getenv("USERNAME", "Unknown"),
        "os_version": os.name,
        "ip_addresses": get_ip_addresses(),
        "running_processes": [proc.info['name'] for proc in psutil.process_iter(['name'])][:5],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return data


def get_ip_addresses():
    ip_addresses = []
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == 2:
                ip_addresses.append(addr.address)
    return ip_addresses
