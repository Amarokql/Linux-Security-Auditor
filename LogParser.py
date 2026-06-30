import subprocess
from ConfirmAction import confirm_action

# Declare a variable to store information about the last 20 SSH login attempts  
def check_ssh_logins(lang):
    try:
        result = subprocess.run(['sudo', 'journalctl', '-u', 'sshd', '-n', '20', '--no-pager'], capture_output=True, text=True)

        # Output the results of checking the last 20 SSH login attempts
        if result.returncode == 0:
            match lang:
                case 'en':
                    print(result.stdout)
                    print('-' * 50)
                    if 'Failed password' in result.stdout:
                        print(f'Failed SSH login attempt {result.stdout.count("Failed password")} from sshd-session') 
                    else:
                        print('No failed SSH login attempts found in the last 20 entries')
                
                case 'ru':
                    print(result.stdout)
                    print('-' * 50)
                    if 'Failed password' in result.stdout:
                        print(f'Неудачная попытка входа по SSH {result.stdout.count("Failed password")} из sshd-session')
                    else:
                        print('Неудачные попытки входа по SSH не найдены в последних 20 записях')
                case _:
                    print("Invalid language choice.")
        else:
            print(f"Error: {result.stderr}")
    except KeyboardInterrupt:
        match lang:
            case 'en':
                print("\nProcess interrupted by user. Exiting...")
            case 'ru':
                print("\nПроцесс прерван пользователем. Выход...")
            
        
        
