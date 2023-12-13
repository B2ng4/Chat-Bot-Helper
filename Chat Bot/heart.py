
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from config import VK_API, PASSWORD
import json
from faq import question, question2
from carousel import create_keyboard_two
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from topics import  GigResponse
import sqlite3
import datetime
# Функция для отправки сообщения



connection = sqlite3.connect('history.db')

cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS History (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL, date TEXT NOT NULL, message TEXT NOT NULL)''')

connection.commit()

def send_message(user_id, message, keyboard=None, template=None):
    vk.messages.send(
        user_id=user_id,
        message=message,
        random_id=0,
        keyboard=keyboard,
        template=json.dumps(template) if template is not None else None
    )

# Функция для создания клавиатуры
def create_keyboard():
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Ответы на частые вопросы', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Задать вопрос', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Сообщить о проблеме', color=VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

# Авторизация бота
vk_session = vk_api.VkApi(token=VK_API)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

# Основной цикл обработки событий
for event in longpoll.listen():
    keyboard = create_keyboard()
    keyboard2 = create_keyboard_two()
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        message = event.text.lower()

        if message == 'начать':
            welcome_message = 'Здравствуйте! Я умный цифровой помощник главы города Мирный. Что Вас интересует?'
            send_message(user_id, welcome_message, keyboard)

        elif message == "ответы на частые вопросы":
            send_message(user_id, "Вы выбрали Ответы на вопросы", template=keyboard2)

        elif message == 'сообщить о проблеме':
            send_message(user_id, 'Вы выбрали "Сообщить о проблеме"')
            send_message(user_id, 'Запишите вашу проблему')
            def received():
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                        received_message = event.text  # Текст сообщения записывается в строку
                        user_id = event.user_id
                        smtp_server = "smtp.yandex.ru"  # Для Gmail. Используйте соответствующий адрес для других провайдеров.
                        smtp_port = 587  # Порт для TLS
                        username = "tchernenkocon@yandex.ru"
                        password = PASSWORD
                        recipient = "timsidorin@gmail.com"
                        message = MIMEMultipart()
                        message["From"] = username
                        message["To"] = recipient
                        message["Subject"] = "Обращение"
                        body = received_message
                        message.attach(MIMEText(body, "plain"))
                        server = smtplib.SMTP(smtp_server, smtp_port)
                        server.starttls()  # Начать шифрованное соединение
                        server.login(username, password)
                        server.send_message(message)
                        server.quit()
                        send_message(user_id, 'Успешно отправлено', keyboard)
                        break
            received()

        elif message == 'задать вопрос':

            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            send_message(user_id, 'Задайте вопрос в свободной форме', keyboard)
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    id = event.user_id
                    user_get = vk.users.get(user_ids=(id))
                    user_get = user_get[0]
                    first_name = user_get['first_name']  # Имя пользователя
                    last_name = user_get['last_name']  # Фамилия
                    full_name = str(first_name+last_name)
                    send_message(user_id, 'Спасибо за вопрос! Идет обработка сообщения........️', keyboard)
                    request = event.text
                    cursor.execute(f'''INSERT INTO History (username,date,message) VALUES ("{full_name}","{current_date}","{request}" )''')
                    connection.commit()
                    send_message(user_id, f'Ваш запрос относится к теме: {GigResponse(request)}', keyboard)
                    break
        #Для частых вопросов
        elif message == 'о жилищных программах':
            send_message(user_id, question(), keyboard)

        elif message == 'о выделении земельных участков':
            send_message(user_id, question2(), keyboard)

        else:
            send_message(user_id, 'Извините, я не понимаю ваш запрос. Пожалуйста, воспользуйтесь клавиатурой.', keyboard)