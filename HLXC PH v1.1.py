Language = input("What language r u use?zh-CN(zh-SG) , zh-TW(zh-HK,zh-MO) or en-UK (en-US)?If u use Chinese(Simplified) type 1,use Chinese(Tranditional) type 2, use English type 3.")
Language = int(Language)

if Language == 1:
    digital = input("Please type the digital!")
    if digital == 'hlsx':
        print("恭喜你，成功输入了密码!")
        print("这串字符的意思是:贺兰是屑!")

    else:
        print('The digital you entered is incorrect! Please enter again!')

if Language == 2:
    digital = input("Please type the digital!")
    if digital == 'hlsx':
        print("恭喜你，成功輸入了密碼！")
        print("這串字符的意思是:賀蘭是屑!")
    else:
        print('The digital you entered is incorrect! Please enter again!')

if Language == 3:
    digital = input("Please type the digital!")
    if digital == 'hlsx':
        print("Congratulations,ur type's digital is right!")
        print("This string mean : shaokeyibb is xie!")
    else:
        print('The digital you entered is incorrect! Please enter again!')
