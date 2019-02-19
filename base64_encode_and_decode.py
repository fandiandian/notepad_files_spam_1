# base64库 加密

import base64

print('默认加密模式')
mode = 'e'
while True :
    rmode = input('请选着模式：加密（e）/或者解密（d）,直接回车表示重复上一次模式,其他字符退出程序\n')
    if rmode == 'd' or rmode == 'e' :    # 这里一定不能写成 rmode == 'd' or 'e' 程序会认为是（rmode == 'd'） or ('e') 导致逻辑错误
        mode = rmode
    elif rmode == '' :
        print('模式不变')
    elif mode != 'd' or mode != 'e' :
        print('程序结束')
        break

    if mode == 'e' :
        s = input('加密模式：请输入要加密的文字:\n')
        t = base64.b64encode(s.encode('utf-8'))
        print(str(t)[2:-1])
    elif mode == 'd' :
        s = input('解密模式：请输入要解密的文字:\n')
        t = base64.b64decode(s)
        print(str(t)[2:-1])
    else :
        print('程序结束')
        break
