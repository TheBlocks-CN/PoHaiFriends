Language = input("What language r u use?zh-CN(zh-SG) , zh-TW(zh-HK,zh-MO) or en-UK (en-US)?If u use Chinese(Simplified) type 1,use Chinese(Tranditional) type 2, use English type 3.")
Language = int(Language)

if Language == 1:
    password = input("Please type the digital!")
    password = int(password)
    if password == 459279:
        print("恭喜你，成功输入了正确的密码!")
        print("这串数字的意思是:贺兰是屑!")

    else:
        print('The password you entered is incorrect! Please enter again!')

if Language == 2:
    password = input("Please type the digital!")
    password = int(password)
    if password == 459279:
        print("恭喜你，成功輸入了密码！")
        print("這串數字的意思是:賀蘭是屑!")
    else:
        print('The password you entered is incorrect! Please enter again!')

if Language == 3:
    password = input("Please type the digital!")
    password = int(password)
    if password == 459279:
        print("Congratulations!ur type's password is right!")
        print("This digital's mean : shaokeyibb is xie!")
    else:
        print('The password you entered is incorrect! Please enter again!')


