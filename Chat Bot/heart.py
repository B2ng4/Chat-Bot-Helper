import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


vk_session = vk_api.VkApi(token = 'vk1.a.BHU7W_4aXKU-DjsygLxNJ6H2Mq9aVHGNlC-F6gmrhJeFmZF8hUsE-Y9_eaprFKJsSfJZJ9FC0doqFLW8_AytL-XqJY3W5huVsGpFHfXT3KEjN1V2xJoLaopwLXX_FcOwEiukY3il3V0oCEL2KSQXqI1NPhsgP3VEPayIhPYOEQLsXwaLxhwgisEBgHBCK9ikoFd4P93Suatj2zZWy5I3bg')
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text,"random_id":0})

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == "hi":
                send_some_msg(id, "Hi kostya!")