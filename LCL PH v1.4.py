print("If you type error,Please Run this py again.")
print("该脚本严格区分大小写，请正确输入'zh-cmn-Hans'等语言代码")
Language = input("What language r u use?zh-cmn-Hans(zh-SG) , zh-cmn-Hant(zh-HK,zh-MO) or English?If u use Chinese(Simplified) type zh-cmn-Hans,use Chinese(Tranditional) type zh-cmn-Hant, use English type en.")

if Language == 'zh-cmn-Hans':
    letter = input("Please input the letter")
    if letter == 'lclsx':
        print("恭喜你!你正确输入了字母!")
        print("'lclsx'的意思是:黎程朗是屑!")
    else:
        print("你输入的字母呢错误!请再次输入!")


if Language == 'zh-cmn-Hant':
    letter = input("Please input the letter")
    if letter == 'lclsx':
        print("恭喜你!你正确输入了字母！")
        print("'lclsx'的意思是:黎程朗是屑！")
    else:
        print("你输入的字母错误!请重新输入!")

if Language == 'en':
    letter = input("Please type the letter!")
    if letter == 'lclsx':
        print("Congratulations!You type letter is right!")
        print("This letter mean Li Chenglang is xie!")
    else:
        print('The letter you entered is incorrect! Please enter again!')


#此版本将变量"Language"的识别方式从"1,2,3"改成ISO 639中的"