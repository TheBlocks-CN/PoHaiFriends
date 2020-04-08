SimplifiedChineseorTranditionalChinese = input("What language are you use?Simplified Chinese or Tranditional Chinese?If you Use Simplified Chinese input 1. If you use Tranditional Chinese input 2.")
SimplifiedChineseorTranditionalChinese = int(input("SimplifiedChineseorTranditionalChinese"))
if SimplifiedChineseorTranditionalChinese == 1:
    password = input("Please input the password")
    password = int(password)
    if password == 9979:
        print("恭喜你!你成功输入了密码!")
        print("9979的意思是:小猪是屑!(9键拼音输入法)")
    else:
        print("你输入的密码错误!请再次输入!")

else:
    password = input("Please input the password")
    password = int(password)
    if password == 9979:
        print("恭喜你!你成功輸入了密碼!")
        print("9979的意思是:小豬是屑!(9键中國大陸拼音输入法)")
    else:
        print("你輸入的密碼錯誤!請重新輸入!")
