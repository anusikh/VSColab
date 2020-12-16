! pip install pyngrok
import getpass
import os
import subprocess
from pyngrok import ngrok

def Connect(password):
    subprocess.call("apt-get install -qq -o=Dpkg::Use-Pty=0 openssh-server pwgen > /dev/null", shell=True)
    subprocess.call(f'echo root:{password} | chpasswd',shell=True)
    subprocess.call('mkdir -p /var/run/sshd', shell=True)
    subprocess.call('echo "PermitRootLogin yes" >> /etc/ssh/sshd_config', shell=True)
    subprocess.call('echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config', shell=True)
    get_ipython().system_raw('/usr/sbin/sshd -D &')
    print("Get your authtoken from https://dashboard.ngrok.com/auth")
    authtoken = getpass.getpass()
    get_ipython().system_raw('./ngrok authtoken $authtoken')
    url = ngrok.connect(22, 'tcp')
    print('Type in terminal $ ssh root@' + ((str(url).split('"')[1::2])[0]).replace('tcp://', '').replace(':', ' -p '))
    print("\tUsername: root")
    print("\tpassword: " + password)

def Kill():
    os.system("kill $(ps aux | grep './ngrok' | awk '{print $2}')")
