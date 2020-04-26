print("The recognition of this script is strictly case sensitive, please enter it correctly！")
print("该脚本严格区分大小写，请正确输入'zh-cmn-Hans'等语言代码")
print("未经允许，请勿转载TheBlocks-CN的''PoHaiFriends'项目，如果您需要转载，请按照CC-BY-NC-SA 4.0协议著名，并且您不能将这份文件商业化使用。")
Language = input("请问你使用什么语言?如果你使用中文(简体)输入zh-cmn-Hans，使用中文(繁体)输入zh-cmn-Hant，使用英语输入en。")

if Language == 'zh-cmn-Hans':
    letter = input("请输入正确的暗号")
    if letter == 'wbtsx':
        print("恭喜你!你正确输入了暗号!")
        print("'wbtsx'的意思是:吴博涛是屑!")
    else:
        print("有内鬼，终止交易!")


if Language == 'zh-cmn-Hant':
    letter = input("請輸入正確的暗號")
    if letter == 'wbtsx':
        print("恭喜你!你正確輸入了暗號！")
        print("'wbtsx'的意思是:吴博涛是屑！")
    else:
        print("你輸入的字母錯誤!請重新輸入!")

if Language == 'en':
    letter = input("Please type the letter!")
    if letter == 'wbtsx':
        print("Congratulations!You type letter is right!")
        print("This letter mean Wu Botao is xie!")
    else:
        print('The letter you entered is incorrect! Please enter again!')


#初版。
#©2020 TheBlocks-CN 版权所有。All Rights Reserved.
#未经允许，请勿转载TheBlocks-CN的"PoHaiFriends"项目，如果您需要转载，请按照CC-BY-NC-SA 4.0协议著名，并且您不能将这份文件商业化使用。

