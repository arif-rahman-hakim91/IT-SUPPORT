import os
import platform
import socket
import wmi
import getpass
import time
import psutil


def clear_screen():
    os.system('cls')

def header_version():
    print('=' * 50)
    print(f'{"IT SUPPORT TOOLKIT v0.2.0":^50}')
    print(f'{"Developed by Arif Rahman Hakim":^50}')
    print('=' * 50)

def info_main():
    print('\nSYSTEM INFORMATION\n')
    print(f'Nama Komputer : {socket.gethostname()}')
    print(f'Nama Pengguna : {getpass.getuser()}')
    print(f'OS            : {platform.system()} {(platform.release())} build {platform.version()}')
    for pro in client.Win32_Processor():
        print(f'Prosessor     : {pro.Name}')
    for gpu in client.Win32_VideoController():
        print(f'GPU           : {gpu.Name}')
    boot = client.Win32_OperatingSystem()[0]
    boot_time = boot.LastBootUpTime
    print(f'Boot Time     : {boot_time[6:8]}-{boot_time[4:6]}-{boot_time[:4]}    {boot_time[8:10]}:{boot_time[10:12]}:{boot_time[12:14]}')
    boot1 = psutil.boot_time()
    uptime = int(time.time() - boot1)
    print(f'System Uptime : {uptime//3600} Hours {(uptime % 3600)//60} Minutes')

def info_perangkat():
    print('\nHARDWARE INFORMATION\n')
    detect = client.Win32_Keyboard()
    if detect:
        for keyboard in detect:
            print(f'Keyboard      : {keyboard.Name}')
            print(f'Status        : {keyboard.Status}')
    else:
        print(f'Keyboard      : Not Detected')
    
    detect = client.Win32_PointingDevice()
    if detect:
        for mouse in detect:
            print(f'Mouse         : {mouse.Name}')
            print(f'Status        : {mouse.Status}')
    else:
        print(f'Mouse         : Not Detected')

    detect = client.Win32_Printer()
    if detect:
        for printer in detect:
            if printer.Default:
                print(f'Printer       : {printer.Name}')
                print(f'Status        : {printer.Status}')
    else:
        print(f'Printer        : Not Detected')

    detect = client.Win32_DesktopMonitor()
    if detect:
        for monitor in detect:
            print(f'Monitor       : {monitor.Name}')
            print(f'Status        : {monitor.Status}')
    else:
        print(f'Monitor        : Not Detected')

    for adapter in client.Win32_NetworkAdapter():
        if (adapter.PhysicalAdapter
            and adapter.NetConnectionStatus == 2
            and 'VirtualBox' not in adapter.Name
            and 'VMware' not in adapter.Name):

            print(f'wifi adapter  : {adapter.Name}')
            print('Status        : Connected\n')

def info_ram():
    v_memory = psutil.virtual_memory()
    print('\nRAM INFORMATION\n')
    print(f'Total RAM     : {round(v_memory.total/(1024**3),2)} GB')
    print(f'Available RAM : {round(v_memory.available/(1024**3),2)} GB')
    print(f'Used RAM      : {round(v_memory.used/(1024**3),2)} GB')
    print(f'Percent Used  : {v_memory.percent}%')
    if v_memory.percent < 70:
        print("RAM usage     : Good ")
        print("Recommendation: No action required ")
    elif 70.00 <= v_memory.percent < 89:
        print("RAM usage     : Fair ")
        print("Recommendation: Close unsued application for best performance ")
    elif v_memory.percent >= 90:
        print("RAM usage     : Warning - High")
        print("Recommendation: close unused application or Restart the Computer ")




    
client = wmi.WMI()
clear_screen()
header_version()
info_main()
info_perangkat()
info_ram()
