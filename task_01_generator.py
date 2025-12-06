import os
import queue as queue_module
import time
import sys

from colorama import init, Fore, Style

init(autoreset=True)

queue = queue_module.Queue()
request_id = 1


def clear_screen():
    """Очистка екрану консолі."""
    os.system("cls" if os.name == "nt" else "clear")


def generate_request():
    """Створення нової заявки та додавання її до черги."""
    global request_id
    request = f"Заявка #{request_id}"
    request_id += 1
    queue.put(request)


def processing_indicator(request):
    """Анімація обробки заявки"""
    spinner = ["|", "/", "-", "\\"]

    print(Fore.YELLOW + f"Обробка {request}")
    for i in range(20):
        frame = spinner[i % len(spinner)]
        sys.stdout.write("\r" + Fore.YELLOW + f"Обробка {frame}")
        sys.stdout.flush()
        time.sleep(0.15)

    # Очистити рядок
    sys.stdout.write("\r" + " " * 30 + "\r")
    sys.stdout.flush()

    print(Fore.GREEN + f"✅ Заявку оброблено: {request}")
    time.sleep(1)


def process_request():
    """Обробка заявки з черги."""
    if queue.empty():
        print(Fore.RED + "!!! Черга порожня, немає що обробляти.")
        time.sleep(1.2)
        return

    request = queue.get()
    processing_indicator(request)


def draw_interface():
    """Відображення інтерфейсу користувача."""
    clear_screen()
    print(Style.BRIGHT + "==== СИСТЕМА ОБРОБКИ ЗАЯВОК ====\n")

    count = queue.qsize()
    color = Fore.GREEN if count > 0 else Fore.YELLOW
    print(color + f"У черзі: {count} заявок\n")

    print(Style.BRIGHT + "Черга:")

    if queue.empty():
        print("  (порожня)")
    else:
        items = list(queue.queue)
        for idx, item in enumerate(items):
            if idx == 0:
                print(f"  {Fore.BLUE}-> {Style.BRIGHT}{item} (наступна до обробки)")
            else:
                print(f"     {Fore.CYAN}{item}")

    print("\nМеню:")
    print(f"{Fore.GREEN}[1]{Style.RESET_ALL} Створити заявку")
    print(f"{Fore.YELLOW}[2]{Style.RESET_ALL} Обробити заявку")
    print(f"{Fore.RED}[0]{Style.RESET_ALL} Вихід")


def main():
    while True:
        draw_interface()
        command = input("\nВведіть команду: ").strip()

        if command == "1":
            generate_request()
        elif command == "2":
            process_request()
        elif command == "0":
            print("Вихід...")
            break
        else:
            print(Fore.RED + "Невідома команда!")
            time.sleep(1)


if __name__ == "__main__":
    main()
