
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from config import VK_API
import requests
import os

# Функция для отправки сообщения
def send_message(user_id, message, keyboard=None):
    vk.messages.send(
        user_id=user_id,
        message=message,
        random_id=0,
        keyboard=keyboard
    )

# Функция для создания клавиатуры
def create_keyboard():
    keyboard = VkKeyboard(one_time=True)

    keyboard.add_button('Подача обращения', color=VkKeyboardColor.PRIMARY)
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
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        message = event.text.lower()

        if message == 'начать':
            welcome_message = 'Здравствуйте! Я умный цифровой помощник главы города Мирный. Что Вас интересует?'
            send_message(user_id, welcome_message, keyboard)

        elif message == 'подача обращения':
            send_message(user_id, 'Вы выбрали "Подача обращения"')
            send_message(user_id, 'Запишите ваше ФИО')
            def name():
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                        user_id = event.user_id
                        full_name = event.text.lower()
                        send_message(user_id, f'Ваше введенное ФИО {full_name}')
                        break
            # name()

            send_message(user_id, 'Запишите ваш населенный пункт')
            def city():
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                        user_id = event.user_id
                        input_city = event.text.lower()
                        send_message(user_id, f'Ваш введенный населенный пункт {input_city}')
                        break
            # city()

            send_message(user_id, 'Запишите вашу электронную почту для обратной связи')
            def email():
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                        user_id = event.user_id
                        input_mail = event.text.lower()
                        send_message(user_id, f'Ваша введенная электронная почта {input_mail}')
                        break
            # email()

            send_message(user_id, 'Прикрепите обращение')


            def download_file(url, file_name, path_to_save, access):
                try:
                    headers = {'Authorization': access}
                    response = requests.get(url, headers=headers)
                    if response.status_code == 200:
                        file_path = os.path.join(path_to_save, file_name)
                        with open(file_path, 'wb') as file:
                            file.write(response.content)
                        print("File downloaded successfully!")
                    else:
                        print("Failed to download file. Status code:", response.status_code)
                except Exception as e:
                    print("An error occurred during file download:", str(e))


            # Usage example
            url = "https://api.vk.com/method/docs.getUploadServer"
            access = 'access_token=vk1.a.FyHTGxC2QiBjahv1ysRJSRNk0tfc1vUmNezj_A0SXBrmodK7G1iPmc-q39FujXH4igSDJtNie7_jklwW-y2w8p_SNfSAbZZXLh5VoL2MeTiE_fSChGqLxUy1RGN19xJtPSMqeHrzHE2dEcc1Qk5MU_y4V7aMyZ-Bims-9yixntUjSWg0aoRebbi7zFBlSK68DWN6IPGCNqBoNkKgaomJfw'
            file_name = "downloaded_file"
            path_to_save = "/home/konstantin/Документы/GitHub/Chat-Bot-Helper/Chat Bot/doc"

            download_file(url, file_name, path_to_save, access)

        elif message == 'ответы на вопросы':
            send_message(user_id, 'Вы выбрали "Ответы на вопросы"',keyboard)

        elif message == 'сообщить о проблеме':
            send_message(user_id, 'Вы выбрали "Сообщить о проблеме"', keyboard)

        elif message == 'задать вопрос':
            send_message(user_id, 'Вы выбрали "Задать вопрос"', keyboard)

        else:
            send_message(user_id, 'Извините, я не понимаю ваш запрос. Пожалуйста, воспользуйтесь клавиатурой.', keyboard)