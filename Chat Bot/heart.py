
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


# Функция для отправки сообщения
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

    keyboard.add_button('Ответы на вопросы', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Сообщить о проблеме', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Задать вопрос', color=VkKeyboardColor.POSITIVE)

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

        elif message == "ответы на вопросы":
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
                        recipient = "lokrit9@gmail.com"
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
            send_message(user_id, 'Вы выбрали "Задать вопрос"', keyboard)

        #Для частых вопросов
        elif message == 'о жилищных программах':
            send_message(user_id, question(), keyboard)

        elif message == 'о выделении земельных участков':
            send_message(user_id, question2(), keyboard)

        else:
            send_message(user_id, 'Извините, я не понимаю ваш запрос. Пожалуйста, воспользуйтесь клавиатурой.', keyboard)