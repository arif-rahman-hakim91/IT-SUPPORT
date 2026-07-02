import os
import platform
import socket
import wmi
import getpass


#membersihkan tampilan awal
def clear_screen():
    os.system("cls")

def info_main():
    print("\nSYSTEM INFORMATION\n")
    print(f"Nama Komputer : {socket.gethostname()}")
    print(f"Nama Pengguna : {getpass.getuser()}")
    print(f"OS            : {platform.system()} {(platform.release())} build {platform.version()}")
    for pro in client.Win32_Processor():
        print(f"Prosessor     : {pro.Name}")
    for gpu in client.Win32_VideoController():
        print(f"GPU           : {gpu.Name}")
    boot = client.Win32_OperatingSystem()[0]
    boot_time = boot.LastBootUpTime
    print(f"Boot Time     : {boot_time[6:8]}-{boot_time[4:6]}-{boot_time[:4]} {boot_time[8:10]}:{boot_time[10:12]}:{boot_time[12:14]}")

def info_perangkat():
    print("\nHARDWARE INFORMATION\n")
    detect = client.Win32_Keyboard()
    if detect:
        for keyboard in detect:
            print(f"Keyboard      : {keyboard.Name}")
            print(f"Status        : {keyboard.Status}\n")
    else:
        print(f"Keyboard      : Not Detected\n")
    
    detect = client.Win32_PointingDevice()
    if detect:
        for mouse in detect:
            print(f"Mouse         : {mouse.Name}")
            print(f"Status        : {mouse.Status}\n")
    else:
        print(f"Mouse         : Not Detected\n")

    detect = client.Win32_Printer()
    if detect:
        for Printer in detect:
            if Printer.Default:
                print(f"Printer       : {Printer.Name}")
                print(f"Status        : {Printer.Status}\n")
    else:
        print(f"Printer        : Not Detected\n")

    detect = client.Win32_DesktopMonitor()
    if detect:
        for monitor in detect:
            print(f"Monitor       : {monitor.Name}")
            print(f"Status        : {monitor.Status}\n")
    else:
        print(f"Monitor        : Not Detected\n")

    for adapter in client.Win32_NetworkAdapter():
        if (adapter.PhysicalAdapter
            and adapter.NetConnectionStatus == 2
            and "VirtualBox" not in adapter.Name
            and "VMware" not in adapter.Name):

            print(f"wifi adapter  : {adapter.Name}")
            print("Status        : Connected\n")
    
client = wmi.WMI()
clear_screen()
info_main()
info_perangkat()
