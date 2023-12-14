
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
        "title": "О выделении земельных участков",
        "description": "Выделение земельных участков многодетным семьям по Закону РС(Я).",
        "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "О выделении земельных участков",
                    "payload": json.dumps({"button": "2"})
                }
            }
        ]
    })

    carousel_elements.append({
        "title": "О правильности начислений ЖКХ",
        "description": "В счетах довольно часто обнаруживаются ошибки.",
        "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "О правильности начислений ЖКХ",
                    "payload": json.dumps({"button": "3"})
                }
            }
        ]
    })

    carousel_elements.append({
        "title": "Способы управления многоквартирным домом.",
        "description": "Какие способы управления многоквартирным домом",
        "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "Способы управления многоквартирным домом",
                    "payload": json.dumps({"button": "4"})
                }
            }
        ]
    })

    carousel_elements.append({
        "title": "Получение земельных участков",
        "description": "Граждане, которые могут получить землю?",
        "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "Получение земельных участков",
                    "payload": json.dumps({"button": "5"})
                }
            }
        ]
    })

    carousel_elements.append({
        "title": "Помощь безработным",
        "description": "Какая существует помощь?",
        "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "Помощь безработным",
                    "payload": json.dumps({"button": "5"})
                }
            }
        ]
    })

    carousel_elements.append({
        "title": "Помощь",
        "description": "Помощь лицам оказавшимся в трудной ситуации",
        "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "Помощь",
                    "payload": json.dumps({"button": "5"})
                }
            }
        ]
    })

    carousel_elements.append({
        "title": "Плата за капитальный ремонт",
        "description": "Для собственников",
        "buttons": [
            {
                "action": {
                    "type": "text",
                    "label": "Плата за капитальный ремонт",
                    "payload": json.dumps({"button": "5"})
                }
            }
        ]
    })

    return {"type": "carousel", "elements": carousel_elements}