
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from config import VK_API

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
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        message = event.text.lower()


        welcome_message = 'Здравствуйте! Я умный цифровой помощник главы города Мирный. Что Вас интересует?'
        keyboard = create_keyboard()
        send_message(user_id, welcome_message, keyboard)

        if message == 'подача обращения':
            send_message(user_id, 'Вы выбрали "Подача обращения"')

        elif message == 'ответы на вопросы':
            send_message(user_id, 'Вы выбрали "Ответы на вопросы"')

        elif message == 'сообщить о проблеме':
            send_message(user_id, 'Вы выбрали "Сообщить о проблеме"')

        elif message == 'задать вопрос':
            send_message(user_id, 'Вы выбрали "Задать вопрос"')

        else:
            send_message(user_id, 'Извините, я не понимаю ваш запрос. Пожалуйста, воспользуйтесь клавиатурой.')

