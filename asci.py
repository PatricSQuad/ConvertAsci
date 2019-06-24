import os
os.system('clear')
logo ='\033[36m╔═╗╔═╗╔╗╔╦  ╦╔═╗╦═╗╔╦╗ asci💙\033[37m v\033[36m0.1\n║  ║ ║║║║╚╗╔╝║╣ ╠╦╝ ║   \033[37m\n╚═╝╚═╝╝╚╝ ╚╝ ╚═╝╩╚═ ╩\n[\033[32m•\033[37m\033[37m]\033[37m Autor    \033[36m: \033[37mgOdenBngsd\n    WhatsApp \033[36m: \033[37m+6281586610616\n    Facebook \033[36m: \033[37mhttps://m.facebook.com/05Asiyap\n    Github   \033[36m: \033[37mhttps://github.com/PatricSQuad'
city = u'💙 + 💙' #<-/// masukan kode assci disini ///#
utf8_encoded = city.encode('utf-8')
print(logo)
print()
print('\033[37m[\033[32m√\033[37m] Kode  \033[36m:  \033[36m')
print(repr(utf8_encoded))
decoded_city = utf8_encoded.decode('utf-8')
print()
print('\033[37m[\033[32m√\033[37m] Hasil \033[36m:  \033[37m ')
print(decoded_city)
print()
print()
print('\033[36mGoodBye Friends\033[37m...')
