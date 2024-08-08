import time
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
from vk_api import VkApi

session = VkApi(token="vk1.a.zmPZ0EML_WQtAuvBnXqrAlJOLE_gJ0tdy1nWTiNetzBbkSB0Px_tP08gJScd10fjhpjr4vEMPZLGDArUuPYE9L9HtlPtdl_e9EifQBztWTPO_S1Kq5k9EEMiNjp_cusdqPqtgM39RPm6IyelMKX8fSzxYmY5EChebqHEl1P2AFuVcekeNXIk2ncWO7EN67mMSWoPpUL1jggBOKhUPpvhwQ")
session_api=session.get_api()
longpoll=VkLongPoll(session)

while True:
   for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(f"Сообщение пришло в: {str(datetime.now())}")
            print(f"Текст сообщения: {str(event.text)}")
            responce = event.text.lower()
            if event.from_user and not event.from_me:
                if responce.find('привет')>=0 or responce.find("здравствуй")>=0:
                    time.slepp(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "И тебе привет!",
                            "random_id": 0,
                        },
                    )
                elif responce.find('как дела')>=0:
                    time.slepp(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "И тебе привет!",
                            "random_id": 0,
                        },
                    )
                elif responce.find('фото')>=0:
                    time.slepp(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "attachment": "photo-9578578_457252650",
                            "random_id": 0,
                        },
                    )
                elif responce.find('видео')>=0:
                    time.slepp(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "attachment": "video-7064585_456258108",
                            "random_id": 0,
                        },
                    )
                
