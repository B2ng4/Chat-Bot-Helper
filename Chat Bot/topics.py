
import config
from gigachat import GigaChat

def GigResponse(text: str):
    giga = GigaChat(credentials="MjQ5ZmE1MmQtNjI3Ni00NjU1LThjOTctNjNhYzgzNGI5M2Q3OjcyMWNiNjNhLThjMDQtNDQ5ZC04ODEwLTcwNGUzZWJhMjE0Yg==", verify_ssl_certs=False)
    response = giga.chat(f"Дано обращение гражданина:{text}. Сопоставь данное обращение с одним из данных заголовков: [Спорт, жилично-комунальное хозяйство, материнский капитал, градо-строительная деятельность, бюджет для граждан, охрана труда, социальные сети, инвестиционная деятельность,защита прав потребителей, раздел имущества, льготы]. Пиши только одним из этих заголовков и ничего лишнего! Выводи ответ в форме: Заголовок")
    return response.choices[0].message.content


