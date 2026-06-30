from main import get_language_choice
from main import lang

def confirm_action(lang, prompt="Вы уверены?") -> bool:
    while True:
        match lang:
            case 'en':
                user_input = input(f"{prompt} (Y/n): ").strip().lower()
                if not user_input or user_input in ('y', 'yes'):
                    return True
                if user_input in ('n', 'no'):
                    return False
                print("Please enter 'y' (yes) or 'n' (no).")
            case 'ru':
                user_input = input(f"{prompt} (Д/н): ").strip().lower()
                if not user_input or user_input in ('д', 'да'):
                    return True
                if user_input in ('н', 'нет'):
                    return False
                print("Пожалуйста, введите 'д' (да) или 'н' (нет).")
            case _:
                print("Invalid language choice.")