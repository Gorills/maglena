import telepot

token = '1844194923:AAGWC399D7A-9npmhBiGjjLWiPd0GDl0NhI'
my_id = 716578030
telegramBot = telepot.Bot(token)

def send_message(text):
    telegramBot.sendMessage(716578030, text, parse_mode="Markdown")