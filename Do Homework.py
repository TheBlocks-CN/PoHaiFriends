print("The recognition of this script is strictly case sensitive, please enter it correctly！")
print("该脚本严格区分大小写，请正确输入'zh-cmn-Hans'等语言代码")
Language = input("请问你使用什么语言?如果你使用中文(简体)输入zh-cmn-Hans，使用中文(繁体)输入zh-cmn-Hant，使用英语输入en。")

if Language == 'zh-cmn-Hans':
    print("全部爬去写作业!")


if Language == 'zh-cmn-Hant':
    print("全部爬去寫作業")


if Language == 'en':
    print("All go to do homework!")