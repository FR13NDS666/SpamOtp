# author : ridho gaming
# contact : facebook.com/tiaajja.tia.39
# plis bang, jan di recode dong:(

import shutil,os,sys,time,requests


if sys.platform in ['nt','win32']:
	os.system('cls')
	W = ''
	R = ''
	G = ''
	Y = ''
	B = ''
	L = ''
	C = ''
else:
	os.system('clear')
	W = '\033[0m'
	R = '\033[91m'
	G = '\033[92m'
	Y = '\033[93m'
	B = '\033[94m'
	L = '\033[95m'
	C = '\033[96m'
try:
	shutil.rmtree('data/__pycache__')
except:
	pass

def banner():
	print ('''
\033[1;96m    _   __           ____
   / | / /_  _____  / __ \____ _____ ___
  /  |/ / / / / _ \/ /_/ / __ `/ __ `__ \\
 / /|  / /_/ /  __/ ____/ /_/ / / / / / /
/_/ |_/\__, /\___/_/    \__,_/_/ /_/ /_/
      /____/\033[0m''')
	print ('\tAuthor  : Ridho Gaming\n\tGithub  : github.com/ridhoNoob\n\tVersion : 1.1')
	print (R+'•'+W+'-'*45+R+'•'+W)
pil = requests.get('http://auxcrewtbdrpg.com/spam.txt').text
banner()
print (str(pil).replace('\\033','\033').replace('\\n','\n'))
print()
choice = input(f'{W}[{L}>{W}] Choice : ')
if choice == '01' or choice == '1':
	import data.mypoin
elif choice == '02' or choice == '2':
	import data.kioson
elif choice == '03' or choice == '3':
	import data.bakmi
elif choice == '04' or choice == '4':
	import data.CodaTsel
elif choice == '05' or choice == '5':
	import data.payu
elif choice == '06' or choice == '6':
	import data.ruparupa
elif choice == '07' or choice == '7':
	import data.KitaBisa
elif choice == '99':
	r = requests.get('http://auxcrewtbdrpg.com/update.txt')
	if 'update' in str(r.text).lower():
		os.system('cd ..;rm -rf SpamOtp; git clone https://github.com/ridhoNoob/SpamOtp')
	else:
		exit('\033[0m[\033[94m*\033[0m] Already To Update')
else:
	exit('\033[91m[!]\033[0m Liat menu dong!')
