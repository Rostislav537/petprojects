import requests

# Замените 'your_bot_token' на токен вашего бота
bot_token = '6501361576:AAHTO-MDxa7IZaSW77Ksn4OoPEth_eI0tLQ'
chat_id = '6525924165'  # Замените 'your_chat_id' на ID чата, куда вы хотите отправить фото

url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

# Открываем файл с изображением в бинарном режиме
with open('photo.png', 'rb') as photo:
    files = {'photo': photo}
    params = {'chat_id': chat_id}
    response = requests.post(url, files=files, params=params)

# Печатаем ответ от сервера Telegram
print(response.json())