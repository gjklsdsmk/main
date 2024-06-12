from fake_headers import Headers
from threading import Thread
from requests import get
from telebot import TeleBot
from io import FileIO
from time import sleep


def try_proxy(proxy):
    all_c.append('')
    try:
        proxies = {'http': f'http://{proxy.replace("http://", "")}', 'https': f'http://{proxy.replace("http://", "")}'}
        get("https://api.ipify.org", proxies=proxies, headers=headers.generate()).text
        print(f'{BOLD + GREEN + proxy.replace("http://", "")} - VALID')
        good_c.add(proxy)
        f.write(proxy.replace("http://", "") + "\n")
    except:
        print(f'{BOLD + RED + proxy.replace("http://", "")} - INVALID')


f = open("good.txt", 'a')
good_c = set()
all_c = list()
bot = TeleBot("7093667487:AAEBK00IkB3W3SW81b2bx7l879tFK-CitWo")
BOLD = '\033[1m'
RED = '\033[91m'
GREEN = '\033[92m'
headers = Headers(headers=True)
proxies = set()
with open("proxy.txt") as file:
    for line in file:
        proxies.add(line.strip())
proxies.remove("")


count = 0
for proxy in proxies:
    sleep(0.05)
    Thread(target=try_proxy, args=(proxy,)).start()
    count += 1
    if len(all_c) % 1000 == 0:
        Thread(target=bot.send_message, args=(6713279525, f"Было проверено уже {len(all_c)}, из них {len(good_c)} валидных")).start()


Thread(target=bot.send_message, args=(6713279525, f"Все потоки были запущены\n+- 2-3 часа и можно писать /proxy")).start()

@bot.message_handler(['proxy'])
def prxlis(_):
    try: f.close() 
    except: ...
    proxiesd = FileIO("good.txt", 'rb')
    proxiesd.name = "good.txt"
    bot.send_document(6713279525, proxiesd.read(), caption="Бля, надеюсь хоть 1к есть\nТут только http/https прокси")


bot.infinity_polling()