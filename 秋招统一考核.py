from Crypto.Hash import SHA256
import base64
import qrcode

def sha256():
    print('这是你需要的方法，请收好。')
    
    str1 = input('请输入需要加密的字符：')
    
    str_1 = SHA256.new()
    str_1.update(str1.encode('utf-8'))
    
    print('加密后：\n',str_1.hexdigest())

def BASE64_1():
    print('这是你需要的方法，请收好。')

    str1 = input('请输入你需要加密的字符：')

    str_1 = base64.b64encode(str1.encode('utf-8'))

    print('这是加密得到的字符：',str(str_1,'utf-8'))

def BASE64_2():
    print('这是你需要的方法，请收好。')
        
    while True:
        try:
            str2 = input('请输入你需要解密的字符：')

            str_2 = base64.b64decode(str2.encode('utf-8'))

            print('这是解密得到的字符：',str(str_2,'utf-8'))

            break
        except:
            while True:
                print('请输入正确的字符串！\n(继续使用请按1，出该功能请按9)')
                skip = input()
                
                while decide(skip) == 0:
                    skip = input('请给予正确指示！')
                else:
                    skip = int(skip)
                    

                while skip != 1 and skip != 9:
                    skip = input('请给予正确指示！')
                        
                    while decide(skip) == 0:
                        skip = input('请给予正确指示！')
                    else:
                        skip = int(skip)

                    if skip == 1 and skip == 9:
                        continue
                
                if skip == 1:
                    print('请继续使用')
                    break
                if skip == 9:
                    break
        if skip == 9:
            break
    print('请选择其他功能')
    
def QRCODE():
    print('这是你需要的方法，请收好。')

    data = input('请输入需要转换的字符：')
    img_file = r'C:\Users\Aki\Desktop\qrcode.png'

    img = qrcode.make(data)
    img.save(img_file)
    img.show()

print('随机事件展开中......')
print('诚实的人啊，')
print('你掉的是：\n1、这个是用sha256加密字符串的方法')
print('2、这个是用base64的加密的方法')
print('3、这个是用base64的解密的方法')
print('4、这个从字符串生成QRcode的方法')

while True:


    choice = input('请输入序号(按9则退出)：')

    def decide(num):
        try:
            num = int(num)
            return True
        except ValueError:
            return False
            
    while decide(choice) == 0:
        choice = input('请输入序号！！！：')
    else:
        choice = int(choice)

    if choice == 1:
        sha256()
    elif choice == 2:
        BASE64_1()
    elif choice == 3:
        BASE64_2()
    elif choice == 4:
        QRCODE()

    if choice == 9:
        break

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 9:
        print('请输入有效序号！！！：')

print('感谢您的使用！')
input()
quit()
