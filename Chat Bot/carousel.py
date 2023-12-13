
import json
def create_keyboard_two():
    carousel_elements = []
    carousel_elements.append({
        "title": "О жилищных программах",
        "description": "О жилищных программах для молодых семей, перечне необходимых документов.",
        "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "О жилищных программах",
                    "payload": json.dumps({"button": "1"})
                }
            }
        ]
    })

    carousel_elements.append({
        "title": "Заголовок 2",
        "description": "Описание 2",
        "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "Кнопка 2",
                    "payload": json.dumps({"button": "2"})
                }
            }
        ]
    })

    carousel_elements.append({
        "title": "Заголовок 3",
        "description": "Описание 3",
        "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "Кнопка 3",
                    "payload": json.dumps({"button": "3"})
                }
            }
        ]
    })

    return {"type": "carousel", "elements": carousel_elements}