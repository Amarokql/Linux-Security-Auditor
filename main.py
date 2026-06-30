import subprocess
from LogParser import check_ssh_logins 
from ShadowPerm import check_shadow_permissions

def get_language_choice() -> str:
   
    print("\nДоступные языки / Available languages:")
    print("[EN] - English\n[RU] - Русский")
    
    while True:
        choice = input("Выберите язык (en/ru): ").strip().lower()
        if choice in ('en', 'ru'):
            return choice
        print("error: Invalid choice. Please select 'en' or 'ru'.")

def main():
    print(check_shadow_permissions())
    print(check_ssh_logins(get_language_choice()))

if __name__ == "__main__":
    main()