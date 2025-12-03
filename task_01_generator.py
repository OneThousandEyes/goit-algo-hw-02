import queue as queue_module
import uuid
import time

#Створити чергу заявок
queue = queue_module.Queue()


def generate_request():
    """Створює нову заявку та додає її до черги"""
    request_id = uuid.uuid4().hex[:8]
    request_data = { 
        'id': request_id, 
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    queue.put(request_data)
    print(f"Заявка {request_id} створена та додана до черги.")
    return request_id


def process_request():
    """Обробляє заявку з черги"""
    if not queue.empty():
        request = queue.get()
        print(f"Обробка заявки {request['id']} з черги.")
        # Імітація обробки заявки
        time.sleep(1)
        print(f"Заявка {request['id']} оброблена.")
    else:
        print("Черга порожня, немає заявок для обробки.")



def main():
Головний цикл програми:
    Поки користувач не вийде з програми:
        Виконати generate_request() для створення нових заявок
        Виконати process_request() для обробки заявок


if __name__ == "__main__":
    main()