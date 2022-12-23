import os
os.system('sudo apt-get update')
os.system('sudo apt install ./install_data/*.deb')
os.system('sudo apt --fix-broken install')
os.system('sudo apt install ./install_data/*.deb')
os.system('ll-cli repo modify https://mirror-repo-linglong.deepin.com/')
if input('安装完毕，是否重启 1是，2否')==str(1):
    os.system('sudo reboot')