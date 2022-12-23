import os
while True:
    text=os.popen('ll-cli list').read()
    print(text)
    a=input('请输入要卸载的程序的APPID以便卸载')
    os.system('ll-cli uninstall '+a)