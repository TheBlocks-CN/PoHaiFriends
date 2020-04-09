Language = input("What language r u use?zh-CN(zh-SG) , zh-TW(zh-HK,zh-MO) or en-UK (en-US)?If u use Chinese(Simplified) type zh-CN,use Chinese(Tranditional) type zh-TW, use English type en-UK.")

if Language == 'zh-CN':
    letter = input("Please type the letter")
    if letter == 'xzsx':
        print("恭喜你!你成功输入了密码!")
        print("xzsx的意思是:小猪是屑!(拼音输入法)")
    else:
        print("你输入的数字错误!请再次输入!")

if Language == 'zh-TW':
    letter = input("Please type the letter")
    if letter == 'xzsx':
        print("恭喜你!你成功輸入了密碼!")
        print("xzsx的意思是:小豬是屑!(中國大陸拼音输入法)")
    else:
        print("你輸入的数字錯誤!請重新輸入!")

if Language == 'en-UK':
    letter = input("Please type the letter")
    if letter == 'xzsx':
        print("Congratulations!You type letter is right!")
        print("The letter 'xzsx' mean:xiaozhu_zty is xie!")
    else:
        print("The letter you entered is incorrect! Please enter again!")

#该版本将Language变量识别方式从"1,2,3"改为语言代码"zh-CN,zh-TW和en-UK"。
