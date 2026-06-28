import subprocess

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
print('-' * 50)

# Declare a variable to store information about the last 20 SSH login attempts  
result = subprocess.run(['sudo', 'journalctl', '-u', 'sshd', '-n', '20', '--no-pager'], capture_output=True, text=True)

# Output the results of checking the last 20 SSH login attempts
if result.returncode == 0:
    print(result.stdout)
    print('-' * 50)
    if 'Failed password' in result.stdout:
        print(f'Failed SSH login attempt {result.stdout.count("Failed password")} from sshd-session') 

else:
    print(f"Error: {result.stderr}")
