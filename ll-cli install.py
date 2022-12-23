import os
while True:
    text=input('请输入软件名称的关键词(en)')
    a=os.popen('ll-cli query '+text).read()
    print(a)
    if a==('app not found in repo\n'):
        print('很抱歉，在玲珑商店中找不到这个软件，可能这个软件的关键词不是这个吧')
    else:
        if input('是否重新搜索？1是，2否')==str(2):
            b=input('请输入这个软件完整的APPID，以便安装')
            os.system('ll-cli install '+b)