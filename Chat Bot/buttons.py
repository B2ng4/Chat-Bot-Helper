

from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def create_keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Ответы на частые вопросы ❓', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('Задать вопрос 📝', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Сообщить о проблеме 🆘', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('История обращений 🕑', color=VkKeyboardColor.SECONDARY)

    return keyboard.get_keyboard()

def back():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Назад', color=VkKeyboardColor.PRIMARY)

    return keyboard.get_keyboard()
