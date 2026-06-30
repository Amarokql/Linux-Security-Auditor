import subprocess

def check_shadow_permissions():
    # Declare a variable to store information about access rights to the /etc/shadow file
    file_shadow_permition = subprocess.run(['sudo', 'ls', '-l', '/etc/shadow'], capture_output=True, text=True)
    permissions = str(file_shadow_permition.stdout).split(": ")[-1].split()[0]

    # Output the results of checking access rights to the /etc/shadow file
    print(f'\nReturn code command "ls -l /etc/shadow": {file_shadow_permition.returncode}')    
    print(f'Permissions file /etc/shadow: {permissions}')
    print('-' * 50)

    # Check if the permissions of the /etc/shadow file are correct and change them if necessary
    if permissions == '-rw-------':
        print('Permissions file /etc/shadow are correct')
    else:
        print('Permissions file /etc/shadow are incorrect')
        subprocess.run(['sudo', 'chmod', '600', '/etc/shadow'])
        print('Permissions file /etc/shadow have been changed to -rw-------')
    print(f'{'-' * 50}\n')
    
