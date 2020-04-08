SCorTC = input("What language r u use?zh-CN(zh-SG) or zh-TW(or zh-HK / zh-MO)?If you Use zh-CN(zh-SG) type 1. If you use zh-TW(or zh-MO / zh-HK) type 2.")
SCorTC = int(input("SCorTC"))
if SCorTC == 1:
    password = input("Please input the password")
    password = int(password)
    if password == 53579:
        print("恭喜你!你成功输入了密码!")
        print("53579的意思是:黎程朗是屑!(9键拼音输入法)")
    else:
        print("你输入的密码错误!请再次输入!")


else:
    password = input("Please input the password")
    password = int(password)
    if password == 53579:
        print("恭喜你!你成功輸入了密碼!")
        print("53579的意思是:黎程朗是屑!(9键中國大陸拼音输入法)")
    else:
        print("你輸入的密碼錯誤!請重新輸入!")
        input()


