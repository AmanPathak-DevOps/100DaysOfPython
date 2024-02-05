import os;

service = input('Enter the Service name to check the status of that Service\n')
state = os.system('systemctl status '+service)