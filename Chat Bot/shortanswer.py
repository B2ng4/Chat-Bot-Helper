# -*- coding: utf-8 -*-
import config
from gigachat import GigaChat

def short_answer(text: str):
    giga = GigaChat(credentials="MjQ5ZmE1MmQtNjI3Ni00NjU1LThjOTctNjNhYzgzNGI5M2Q3OjcyMWNiNjNhLThjMDQtNDQ5ZC04ODEwLTcwNGUzZWJhMjE0Yg==", verify_ssl_certs=False)
    response = giga.chat(f"Составь очень краткий ответ на вопрос жителя:{text}.Напиши ответ не более 1-2 предложений")
    return response.choices[0].message.content