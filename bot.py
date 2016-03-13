import sys
import time
import telepot
import urllib


SERVERS = ['euro217.vpnbook.com', 'euro214.vpnbook.com',
           'us1.vpnbook.com', 'us2.vpnbook.com', 'ca1.vpnbook.com',
           'de233.vpnbook.com']

def handle(msg):
    text = msg['text']
    chat_id = msg['chat']['id']

    if text == '/start':
        show_keyboard = {'keyboard': [['/server', '/password']]}
        bot.sendMessage(chat_id, 'Server or Password? http://www.vpnbook.com/#pptpvpn', reply_markup=show_keyboard)

    elif text == '/server':
        for server in SERVERS:
            bot.sendMessage(chat_id, server)

    elif text == '/password':
        f = urllib.urlopen("http://www.vpnbook.com")
        b = f.read()
        f.close()
        pwd = find_between(b, "Password: ", "</strong>")
        bot.sendMessage(chat_id, pwd)


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


# Getting the token from command-line is better than embedding it in code,
# because tokens are supposed to be kept secret.
TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)

print 'Listening ...'

# Keep the program running.
while 1:
    time.sleep(10)
