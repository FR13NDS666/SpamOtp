import os,sys,time,requests,mechanize
from fake_useragent import UserAgent

head = {
	'Host': 'nabill.me',
	'accept':'*/*',
	'x-requested-with':'XMLHttpRequest',
	'user-agent':UserAgent().random,
	'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
	'origin':'https://nabill.me',
	'sec-fetch-site':'same-origin',
	'sec-fetch-mode':'cors',
	'referer':'https://nabill.me/Bakmi_Otp',
	'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	}

class bot:
	def __init__(self,nomor,jumlah):
		self.nomor = nomor
		self.jumlah = jumlah
		print()
		self.otw()
	def otw(self):
		for i in range(1,int(self.jumlah)+1):
			r = requests.post('https://nabill.me/Tools/Prank-Tools/Bakmi/api.php',headers=head,data=
			{
				'nomor':self.nomor,
				'jumlah':'1'
			})
			if 'Terkirim' in str(r.text):
				print (f'\033[0m[\033[92m{i}\033[0m] Sukses Terkirim Ke \033[95m{self.nomor}\033[0m')
			else:
				print (r.text)
			time.sleep(2)

while True:
	try:
		nomor = input('\033[96m[+]\033[0m No Hp (62) : ')
		if nomor == '':
			exit('\033[91m[!]\033[0m Jangan Kosong Gan!')
		if '08' in nomor[0:2]:
			exit('\033[91m[!]\033[0m Pakai 62 Gan!')
		jumlah = input('\033[96m[+]\033[0m Jumlah : ')
		if jumlah == '':
			exit('\033[96m[!]\033[0m Jangan Kosong Gan!')
		bot(nomor,jumlah)
		exit()
	except KeyboardInterrupt:
		exit('\n')
