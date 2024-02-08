import paramiko
import os

def ssh_to_machine(server_list,username,auth_method,auth_value,command):
    for server in server_list:
        try:
            ssh_client = paramiko.client.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            if auth_method == 'password':
                ssh_client.connect(server,username=username,password=auth_value)
            elif auth_method == 'pem':
                ssh_key = paramiko.RSAKey.from_private_key_file(auth_value)
                ssh_client.connect(hostname=server,username=username,pkey=ssh_key)
        
            stdin, stdout, stderr = ssh_client.exec_command(command)

            output = stdout.read().decode()

            print(f'Output from {server}')
            print(output)

            ssh_client.close()

        except paramiko.AuthenticationException:
            print(f'Authentication failed for {server}')
        except paramiko.SSHException as e:
            print(f'SSH Connection failed for {server}: {e}')
        except Exception as e:
            print(f'An error occured on the {server}: {e}')

server_list = ["34.229.91.20"]

username = 'ubuntu'
auth_method = 'password'
auth_value = 'admin1'
command = 'df -h'

ssh_to_machine(server_list,username,auth_method,auth_value,command)