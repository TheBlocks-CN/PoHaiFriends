Language = input("What language r u use?zh-CN(zh-SG) , zh-TW(zh-HK,zh-MO) or en-UK (en-US)?If u use Chinese(Simplified) type 1,use Chinese(Tranditional) type 2, use English type 3.")
Language = int(Language)
if Language == 1:
    digital = input("Please input the digital")
    digital = int(digital)
    if digital == 53579:
        print("恭喜你!你成功输入了数字!")
        print("53579的意思是:黎程朗是屑!(9键拼音输入法)")
    else:
        print("你输入的数字错误!请再次输入!")


if Language == 2:
    digital = input("Please input the digital")
    digital = int(digital)
    if digital == 53579:
        print("恭喜你!你成功輸入了數字!")
        print("53579的意思是:黎程朗是屑!(9键中國大陸拼音输入法)")
    else:
        print("你輸入的數字錯誤!請重新輸入!")

if Language == 3:
    digital = input("Please type the digital!")
    digital = int(digital)
    if digital == 53579:
        print("Congratulations!You type digital is right!")
        print("This Digital mean Li Chenglang is xie!")
    else:
        print('The digital you entered is incorrect! Please enter again!')


#此版本新增English (英语) 并将变量更改为合适描述。(password -> digital)


