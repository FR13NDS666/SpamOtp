#Author : Ridho Gaming
#Jangan di recode dong bang, ga kasian ama aing apa:(

import os,sys,time,requests
from fake_useragent import UserAgent

head = {
	'Host':'nabill.me',
	'accept':'*/*',
	'x-requested-with':'XMLHttpRequest',
	'user-agent':UserAgent().random,
	'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
	'origin':'https://nabill.me',
	'sec-fetch-site':'same-origin',
	'sec-fetch-mode':'cors',
	'referer':'https://nabill.me/Codashop_Spam_Telkomsel',
	'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
	}

class Spam:
	def __init__(self,nomor,jumlah):
		self.nomor = nomor
		self.jumlah = jumlah
		print()
		self.otw()
	def otw(self):
		for i in range(1,int(self.jumlah)+1):
			r = requests.post('https://nabill.me/Tools/Prank-Tools/Codashop-Spam-Telkomsel/api.php',headers=head,data=
			{
				'nomor':self.nomor,
				'jumlah':'1'
			})
			if 'Terkirim' in str(r.text):
				print (f'\033[0m[\033[92m{i}\033[0m] Sukses Terkirim Ke \033[95m{self.nomor}\033[0m')
			elif 'Gagal' in str(r.text):
				print (f'[\033[91m{i}\033[0m] Gagal Terkirim Ke \033[95m{self.nomor}\033[0m')
			else:
				exit(r.text)
			time.sleep(2)

while True:
	try:
		nomor = input('\033[96m[+]\033[0m No Hp : ')
		if nomor == '':
			exit('\033[91m[!]\033[0m Jangan Kosong Gan!')
		jumlah = input('\033[96m[+]\033[0m Jumlah : ')
		if jumlah == '':
			exit('\033[91m[!]\033[0m Jangan Kosong Gan!')
		Spam(nomor,jumlah)
		exit()
	except KeyboardInterrupt:
		exit('\n')
