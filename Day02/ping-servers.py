import subprocess

server = input('Enter the domain name or public Ip to check whether it is pinging or not?\n')

response = subprocess.run(['ping', '-c', '1', server], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if response.returncode == 0:
    print('The Given Server is Reachable')
else:
    print('The Given Server is not Reachable')