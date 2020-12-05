import getpass
import os
import subprocess

def Connect(password):
    subprocess.call("apt-get install -qq -o=Dpkg::Use-Pty=0 openssh-server pwgen > /dev/null", shell=True)
    subprocess.call(f'echo root:{password} | chpasswd',shell=True)
    subprocess.call('mkdir -p /var/run/sshd', shell=True)
    subprocess.call('echo "PermitRootLogin yes" >> /etc/ssh/sshd_config', shell=True)
    subprocess.call('echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config', shell=True)
    print("username: root")
    print("password: ", password)
    get_ipython().system_raw('/usr/sbin/sshd -D &')
    subprocess.call('wget -q -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip',shell=True)
    subprocess.call('unzip -qq -n ngrok-stable-linux-amd64.zip', shell=True)
    print("Get your authtoken from https://dashboard.ngrok.com/auth")
    authtoken = getpass.getpass()
    get_ipython().system_raw('./ngrok authtoken $authtoken && ./ngrok tcp 22 &')

def VSConfig(str):
    print("Host VSConfig")
    print(f"\tHostName {str[6:20]}")
    print("\tUser root")
    print(f"\tPort {str[21:26]}")

def Kill():
    os.system("kill $(ps aux | grep './ngrok' | awk '{print $2}')")