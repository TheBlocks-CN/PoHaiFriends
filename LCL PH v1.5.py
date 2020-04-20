print("The recognition of this script is strictly case sensitive, please enter it correctly！")
print("该脚本严格区分大小写，请正确输入'zh-cmn-Hans'等语言代码")
Language = input("请问你使用什么语言?如果你使用中文(简体)输入zh-cmn-Hans，使用中文(繁体)输入zh-cmn-Hant，使用英语输入en。")

if Language == 'zh-cmn-Hans':
    letter = input("请输入正确的暗号")
    if letter == 'lclsx':
        print("恭喜你!你正确输入了暗号!")
        print("'lclsx'的意思是:黎程朗是屑!")
    else:
        print("有内鬼，终止交易!")


if Language == 'zh-cmn-Hant':
    letter = input("請輸入正確的暗號")
    if letter == 'lclsx':
        print("恭喜你!你正確輸入了暗號！")
        print("'lclsx'的意思是:黎程朗是屑！")
    else:
        print("你輸入的字母錯誤!請重新輸入!")

if Language == 'en':
    letter = input("Please type the letter!")
    if letter == 'lclsx':
        print("Congratulations!You type letter is right!")
        print("This letter mean Li Chenglang is xie!")
    else:
        print('The letter you entered is incorrect! Please enter again!')


#此版本将开头"input"的字样改成了中文。


