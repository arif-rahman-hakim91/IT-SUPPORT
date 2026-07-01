import os
import platform
import socket
import wmi


#membersihkan tampilan awal
def sapu():
    os.system("cls")

def info_main():
    print("\nSYSTEM INFORMATION\n")
    print(f"Nama Komputer : {socket.gethostname()}")
    print(f"OS            : {platform.system()} {(platform.release())} {platform.version()}")
    for pro in client.Win32_Processor():
        print(f"Prosessor     : {pro.Name}")
    for gpu in client.Win32_VideoController():
        print(f"GPU           : {gpu.Name}")

def info_perangkat():
    print("\nHARDWARE INFORMATION\n")
    for key in client.Win32_Keyboard():
        print(f"Keyboard      : {key.Name} status : {key.status}")
    for mouse in client.Win32_PointingDevice():
        print(f"Mouse         : {mouse.Name} status : {mouse.status}")
    for printer in client.Win32_Printer():
        if printer.Default:
            print(f"printer       : {printer.Name} status : {printer.status}")
    for monitor in client.Win32_DesktopMonitor():
        print(f"Monitor       : {monitor.Name} status : {monitor.status}")
    
client = wmi.WMI()
sapu()
info_main()
info_perangkat()
