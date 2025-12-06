import os
import time
import sys
from collections import deque

from colorama import init, Fore, Style

init(autoreset=True)


def clear_screen():
    """Очистка екрану консолі."""
    os.system("cls" if os.name == "nt" else "clear")


def normalize_text(text: str) -> str:
    """Нормалізуємо рядок"""
    return "".join(ch.lower() for ch in text if not ch.isspace())


def processing_indicator():
    """Анімація перевірки рядка."""
    spinner = ["|", "/", "-", "\\"]
    for i in range(20):
        frame = spinner[i % len(spinner)]
        sys.stdout.write("\r" + Fore.YELLOW + f"Перевірка {frame}")
        sys.stdout.flush()
        time.sleep(0.1)

    # Очистити рядок
    sys.stdout.write("\r" + " " * 30 + "\r")
    sys.stdout.flush()


def is_palindrome(text: str) -> bool:
    """Перевірка, чи є рядок паліндромом"""
    normalized = normalize_text(text)
    d = deque(normalized)

    while len(d) > 1:
        left = d.popleft()
        right = d.pop()
        if left != right:
            return False
    return True


# Глобальні змінні для "інтерфейсу"
last_input = ""
last_result = None  # None / True / False
last_normalized = ""


def draw_interface():
    """Відображення інтерфейсу користувача."""
    clear_screen()
    print(Style.BRIGHT + "==== ПЕРЕВІРКА РЯДКА НА ПАЛІНДРОМ ====\n")

    if last_input:
        print(Style.BRIGHT + "Останній введений рядок:" + Style.RESET_ALL)
        print(f"  {Fore.CYAN}{last_input}{Style.RESET_ALL}\n")

        print(Style.BRIGHT + "Нормалізований варіант (для перевірки):" + Style.RESET_ALL)
        print(f"  {Fore.BLUE}{last_normalized or '(порожній)'}{Style.RESET_ALL}\n")

        if last_result is True:
            print(Fore.GREEN + "✅ Це паліндром\n")
        elif last_result is False:
            print(Fore.RED + "❌ Це не паліндром\n")
    else:
        print(Fore.YELLOW + "Рядок ще не було введено.\n")

    print("Меню:")
    print(f"{Fore.GREEN}[1]{Style.RESET_ALL} Ввести новий рядок")
    print(f"{Fore.RED}[0]{Style.RESET_ALL} Вихід")


def main():
    global last_input, last_result, last_normalized

    while True:
        draw_interface()
        command = input("\nВведіть команду: ").strip()

        if command == "1":
            clear_screen()
            print(Style.BRIGHT + "Введення рядка для перевірки на паліндром:\n")
            user_text = input("Введіть рядок: ")

            last_input = user_text
            last_normalized = normalize_text(user_text)

            # Анімація "перевірки"
            processing_indicator()

            # Перевірка паліндрому
            last_result = is_palindrome(user_text)

        elif command == "0":
            print("Вихід...")
            break
        else:
            print(Fore.RED + "Невідома команда!")
            time.sleep(1)


if __name__ == "__main__":
    main()
