import platform
import os
import socket
import ctypes
import shutil

total, used, free = shutil.disk_usage("/")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))


def windows():
    users = str(os.popen("net user").read())
    x = (users.rsplit()[5:10:1])

    user32 = ctypes.windll.user32
    screensize = (user32.GetSystemMetrics(0)), (user32.GetSystemMetrics(1))

    cpu = str(os.popen("wmic cpu get name").read())
    cpu_name = cpu.rsplit()[1::1]
    cpu2 = str(cpu_name).strip("[]").replace(",", " ").replace("'", " ")

    boot_time = str(os.popen('systeminfo | find "System Boot Time"').read())

    print("[+] CPU Type: " + platform.processor())
    print("[+] CPU Name: " + cpu2)
    print("[+] OS: " + platform.system())
    print("[+] Machine: " + platform.machine())
    print("[+] OS Release: " + platform.release())
    print("[+] Host name: " + platform.node())
    print("[+] Machine Platform: " + platform.platform())
    print("[+] Architect: " + platform.architecture()[0])
    print("[+] Login Name :" + os.getlogin())
    print("[+] Local IP: " + s.getsockname()[0])
    print("[+] Resolution: " + str(screensize).replace(",", " X"))
    print("[+] Users: " + str(x).strip("[],").replace("'", " "))
    print("[+] " + boot_time)
    print("[+] Hard drive: \n\t\t\t\t" + "Total: %d GB" % (total // (2 ** 30)) + "\n\t\t\t\t""Used: %d GB"
          % (used // (2 ** 30))
          + "\n\t\t\t\t" + "Free: %d GB" % (free // (2 ** 30)))


def linux():
    kernel_version = os.popen("uname -v").read()
    kernel = os.popen("uname -or").read()
    cpu_name = os.popen("lscpu | grep name").read()
    users = os.popen("awk -F':' '{ print $1}' /etc/passwd").read()
    os_version = os.popen("uname -o").read()
    boot_time_linux = os.popen("uptime").read()
    system_resu = os.popen("xdpyinfo | grep dimensions ").read()

    print("[+] Kerel : " + kernel)
    print("[+] Kernel Version: " + kernel_version)
    print("[+] CPU Name: " + cpu_name)
    print("[+] OS: " + platform.system())
    print("[+] OS Version: " + os_version)
    print("[+] Machine: " + platform.machine())
    print("[+] OS Release: " + platform.release())
    print("[+] Host name: " + platform.node())
    print("[+] Machine Platform: " + platform.platform())
    print("[+] Architect: " + platform.architecture()[0])
    print("[+] Login Name :" + os.getlogin())
    print("[+] Local IP: " + s.getsockname()[0])
    print("[+] Resolution: " + system_resu)
    print("[+] Boot Time: " + boot_time_linux)
    print("[+] Users: " + str(users.rsplit()).strip("[]").replace("'", " "))
    print("\n[+] Hard drive: \n\t\t\t\t" + "Total: %d GB" % (total // (2 ** 30)) + "\n\t\t\t\t""Used: %d GB"
          % (used // (2 ** 30))
          + "\n\t\t\t\t" + "Free: %d GB" % (free // (2 ** 30)))
def main():

    print("Welcome To System Information script:\n ")
    print("Please Chose The System You Want To Check For Information: \n1. Windows \n2. Linux\n")
    user_choice = int(input("So What Have You Chose:"))
    if user_choice == 1:
        print("\nOk Let's Work On Windows System \n")
        windows()
        print("\n***** The Job As Done Thank You <3 *****")
    else:
        print("\nOk Let's Work On Linux System \n")
        linux()
        print("\n******* The Job As Done Thank You <3 ******")
if __name__ == '__main__':
    main()

exit()
