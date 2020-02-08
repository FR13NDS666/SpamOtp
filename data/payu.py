#/usr/bin/python3.7
# -*- Coding: utf-8 -*-
# Author : Ridho Gaming

import os,requests,time,sys,re,mechanize
from bs4 import BeautifulSoup as sup

if sys.platform in ['nt','win32']:
	W = ""
	G = ""
	B = ""
	Y = ""
	C = ""
	R = ""
else:
	W = '\033[0m'
	G = '\033[92m'
	B = '\033[94m'
	Y = '\033[93m'
	C = '\033[96m'
	R = '\033[91m'

kepala = {
	"Host":"sms.payuterus.biz",
	"Connection":"keep-alive",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Linux; Android 9; RMX1911 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
	"Accept-Encoding":"gzip, deflate",
	"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	"X-Requested-With":"com.smsGratisSeluruhIndonesia64"
}
url = "http://sms.payuterus.biz/alpha/"
def GetAll():
	global c
	c = requests.Session()
	r = c.get(url,headers=kepala)
	cfduid = re.findall("(?<=__cfduid=)(.*?);",str(r.headers['Set-Cookie']))[0]
	sesi = re.findall("(?<=PHPSESSID=)(.*?);",str(r.headers['Set-Cookie']))[0]
	o = []
	html = sup(r.content,features='html.parser')
	for hasil in html.find_all('span'):
		o.append(hasil.text)
	capt = int(str(o)[2])+int(str(o)[6])
	parsing = sup(r.content,features='html.parser')
	hmm = parsing.find_all('input')[4]
	key = re.findall('(?<=value=)"(.*?)"',str(hmm))[0]
	return {
	"cfduid":cfduid,
	"sesi":sesi,
	"capt":capt,
	"key":key
}
class Payu:
	def __init__(self):
		self.nomor()
	def nomor(self):
		self.nohp = input("\033[96m[+]\033[0m No Hp : "+G)
		if self.nohp == "":
			self.nomor()
		else:
			self.hoh()
	def hoh(self):
		print (f"{Y}[INFO] Type <n> for new line")
		self.pesan = input(W+"\033[96m[+]\033[0m Pesan : ").replace('<n>','\n')
		if self.pesan == "":
			self.hoh()
		else:
			self.mulai()
	def mulai(self):
		haha = GetAll()
		head = {
	"Host":"sms.payuterus.biz",
	"Connection": "keep-alive",
	"Origin": "http://sms.payuterus.biz",
	"Upgrade-Insecure-Requests": "1",
	"Content-Type": "application/x-www-form-urlencoded",
	"User-Agent": "Mozilla/5.0 (Linux; Android 9; RMX1911 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
	"Referer": "http://sms.payuterus.biz/alpha/",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	"Cookie":"__cfduid="+str(haha['cfduid'])+"; PHPSESSID="+str(haha['sesi'])+"; _ga=GA1.2.655696824.1580558326; _gid=GA1.2.978964674.1580558326; __gads=ID=2dc1d11dac483254:T=1580558326:S=ALNI_Mb1RnVJ0hJfGQdEjsud9zl_AhDa-Q; _gat=1",
	"X-Requested-With":"com.smsGratisSeluruhIndonesia64"
}
		r = c.post(url+'send.php',headers=head,data={
	"nohp":self.nohp,
	"pesan":self.pesan,
	"captcha":haha['capt'],
	"key":haha['key']
})
		if 'SMS Gratis Telah Dikirim' in str(r.text):
			print (f"{W}[{G}✓{W}] Sukses Terkirim Ke{C}",self.nohp,W)
		else:
			print ('[!] Gagal terkirim ke{R}',self.nohp,W)
while True:
	try:
		Payu()
		break
	except KeyboardInterrupt:
		exit('\n')
	except Exception as E:
		exit(f'[Err] : {E}')
	except:
		pass
