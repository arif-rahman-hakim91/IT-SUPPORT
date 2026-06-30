import os
import platform
import socket
import wmi


#membersihkan tampilan awal
def sapu():
    os.system("cls")

def info_perangkat():
    print("\nINFORMASI PERANGKAT\n")
    print(f"Nama Komputer : {socket.gethostname()}")
    print(f"OS            : {platform.system()} {(platform.release())} {platform.version()}")
    a = wmi.WMI()
    for b in a.Win32_Processor():
        print(f"Prosessor     : {b.Name}")
    a = wmi.WMI()
    for b in a.Win32_VideoController():
        print(f"GPU           : {b.Name}")

sapu()
info_perangkat()
