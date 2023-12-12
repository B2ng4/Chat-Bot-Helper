import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import  VK_API

vk_session = vk_api.VkApi(token=VK_API)
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