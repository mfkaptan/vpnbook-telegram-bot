import sys
import time
import telepot
import urllib.request


SERVERS = ['euro217.vpnbook.com', 'euro214.vpnbook.com',
           'us1.vpnbook.com', 'us2.vpnbook.com', 'ca1.vpnbook.com',
           'de233.vpnbook.com']


class VPNBoot(telepot.Bot):
    def __init__(self, *args, **kwargs):
        super(VPNBoot, self).__init__(*args, **kwargs)

    def handle(self, msg):
        flavor = telepot.flavor(msg)
        if flavor != "chat":
            return

        text, chat_id = None, None

        try:
            content_type, chat_type, chat_id = telepot.glance(msg)
            text = msg['text']
        except:
            return
        else:
            if content_type != "text":
                return

        if text == '/start':
            show_keyboard = {'keyboard': [['/server', '/password']]}
            bot.sendMessage(chat_id, 'Server or Password? http://www.vpnbook.com/#pptpvpn', reply_markup=show_keyboard)

        elif text == '/server':
            for server in SERVERS:
                bot.sendMessage(chat_id, server)

        elif text == '/password':
            with urllib.request.urlopen("http://www.vpnbook.com") as url:
            	html = str(url.read())
            
            pwd = self.find_between(html, "Password: ", "</strong>")
            bot.sendMessage(chat_id, pwd)

    def find_between(self, s, first, last):
        try:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            return s[start:end]
        except ValueError:
            return ""


# Getting the token from command-line is better than embedding it in code,
# because tokens are supposed to be kept secret.
TOKEN = sys.argv[1]

bot = VPNBoot(TOKEN)
bot.message_loop()

print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
