
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from config import VK_API, PASSWORD
import json
from faq import *
from carousel import create_keyboard_two
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from topics import  GigResponse
import sqlite3
import datetime
from better_profanity import profanity
from urllib.request import urlretrieve
from email.mime.image import MIMEImage
import requests
from NLP import bert_semantic_similarity as nlp
import shortanswer
from toxic import insult

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
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Ответы на частые вопросы ❓', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Задать вопрос 📝', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Сообщить о проблеме 🆘', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('История обращений 🕖', color=VkKeyboardColor.SECONDARY)

    return keyboard.get_keyboard()

def back():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()

# Авторизация бота
vk_session = vk_api.VkApi(token=VK_API)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

# Основной цикл обработки событий
for event in longpoll.listen():
    keyboard = create_keyboard()
    keyboard2 = create_keyboard_two()
    b_back = back()
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        message = event.text.lower()

        if message == 'начать':
            welcome_message = 'Здравствуйте! Я умный цифровой помощник главы города Мирный. Что Вас интересует?'
            send_message(user_id, welcome_message, keyboard)

        elif message == "ответы на частые вопросы ❓":
            send_message(user_id, "Вы выбрали Ответы на вопросы", template=keyboard2)
            send_message(user_id, "Ответы на частые вопросы👆", keyboard)

        elif message == 'сообщить о проблеме 🆘':
            send_message(user_id, 'Вы выбрали "Сообщить о проблеме"')
            send_message(user_id, 'Запишите вашу проблему, также приложите фотоснимок(если он есть)', b_back)
            def received():
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                        received_message = event.text  # Текст сообщения записывается в строку
                        user_id = event.user_id
                        if event.text == "Назад":
                            send_message(user_id, 'Возврат в главное меню', keyboard)
                            break
                        else:
                            smtp_server = "smtp.yandex.ru"  # Для Gmail. Используйте соответствующий адрес для других провайдеров.
                            smtp_port = 587  # Порт для TLS
                            username = "tchernenkocon@yandex.ru"
                            password = PASSWORD
                            recipient = "lokrit9@gmail.com"
                            email_message = MIMEMultipart()
                            email_message["From"] = username
                            email_message["To"] = recipient
                            email_message["Subject"] = "Обращение"
                            body = received_message
                            email_message.attach(MIMEText(body, "plain"))
                            messages = vk.messages.getHistory(count=5, user_id=user_id)['items']
                            # Поиск изображений в сообщениях
                            for message in messages:
                                if 'attachments' in message:
                                    for attachment in message['attachments']:
                                        if attachment['type'] == 'photo':
                                            # Получение URL самой большой версии изображения
                                            photo_url = max(attachment['photo']['sizes'], key=lambda size: size['height'])[
                                                'url']
                                            # Скачивание изображения
                                            urlretrieve(photo_url, "pict/downloaded_image.jpg")
                                            print("Изображение скачано")
                                            break

                            for msg in messages:
                                if 'attachments' in msg:
                                    for attachment in msg['attachments']:
                                        if attachment['type'] == 'photo':
                                            photo_url = max(attachment['photo']['sizes'], key=lambda size: size['height'])['url']
                                            response = requests.get(photo_url)
                                            img = MIMEImage(response.content)
                                            email_message.attach(img)
                                            print("Изображение прикреплено к письму")
                                            break

                            server = smtplib.SMTP(smtp_server, smtp_port)
                            server.starttls()  # Начать шифрованное соединение
                            server.login(username, password)
                            server.send_message(email_message)
                            server.quit()
                            send_message(user_id, 'Успешно отправлено', keyboard)
                            break
            received()

        elif message == 'задать вопрос 📝':
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            send_message(user_id, 'Задайте вопрос в свободной форме')
            send_message(user_id, 'Для возврата в главное меню нажмите кнопку "Назад"', b_back)
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    if event.text == "Назад":
                        send_message(user_id, 'Возврат в главное меню', keyboard)
                        break
                    else:
                        request = event.text
                        if 1:
                            id = event.user_id
                            insult()
                            if profanity.contains_profanity(request):  # Проверка на наличие нецензурных слов
                                    send_message(user_id,'❗️❗️Я не могу обработать данный запрос\nПрисутсвуют некорректные слова❗️❗️️',keyboard)
                                    break
                            else:
                                user_get = vk.users.get(user_ids=(id))
                                user_get = user_get[0]
                                first_name = user_get['first_name']  # Имя пользователя
                                last_name = user_get['last_name']  # Фамилия
                                full_name = str(first_name+last_name)
                                send_message(user_id, 'Спасибо за вопрос! Идет обработка сообщения ♾️♾️♾️.️', keyboard)
                                cursor.execute(f'''INSERT INTO History (username,date,message) VALUES ("{full_name}","{current_date}","{request}" )''')
                                connection.commit()
                                link = nlp(event.text)
                                send_message(user_id, f'Ваш запрос относится к теме: 👉{GigResponse(request)}👈\n', keyboard)
                                short_ans = shortanswer.short_answer(event.text)
                                send_message(user_id, f"🕐 Краткий ответ:\n {short_ans}" , keyboard)
                                send_message(user_id, f'👉{link}👈 \n По данной ссылке расположен документ, который может вам помочь!', keyboard)
                                break
                        # else:
                        #     send_message(user_id, '❗️❗️Я не могу обработать данный запрос\nПрисутсвуют некорректные слова❗️❗️️', keyboard)
                        #     break



        #Для частых вопросов
        elif message == 'о жилищных программах':
            send_message(user_id, question(), keyboard)

        elif message == 'о выделении земельных участков':
            send_message(user_id, question2(), keyboard)

        elif message == 'о правильности начислений жкх':
            send_message(user_id, question3(), keyboard)

        elif message == 'способы управления многоквартирным домом':
            send_message(user_id, question4(), keyboard)

        elif message == 'получение земельных участков':
            send_message(user_id, question5(), keyboard)

        elif message == 'помощь безработным':
            send_message(user_id, question6(), keyboard)

        elif message == 'помощь':
            send_message(user_id, question7(), keyboard)

        elif message == 'плата за капитальный ремонт':
            send_message(user_id, question8(), keyboard)

        else:
            send_message(user_id, 'Извините, я не понимаю ваш запрос. Пожалуйста, воспользуйтесь клавиатурой.', keyboard)