import os
print('''WTP016的菜单
-------------------
 [1] 启动 Google Chrome             [9] 启动 哔哩 UWP客户端
 [2] 启动 PCL 2                     [10] 启动 Discord
 [3] 启动 NtrQQ 9.2.5               [11] 启动 OBS Studio
 [4] 启动 Photoshop 2020            [12] 启动 Windows Terminal
 [5] 启动 Premiere Pro 2020         [13] 启动 设置
 [6] 启动 Ashampoo WinOptimizer 18  [14] 启动 Firefox
 [7] 启动 JustProxy or SSTap        [15] 启动 网易云音乐
 [8] 启动 Wechat PC Client          [16] 启动 Viusal Studio Code
 
 
 [17] 启动 Dism ++
 [18] 启动 菜单 CMD 版
 [19] 退出该菜单
-------------------
 ''')
select = int(input("↑ 输入 [] 里对应的内容进行选择 : "))

if select == 1:
    os.system('G:\pyzy\gc.lnk')
    exit()

if select == 2:
    os.system('G:\pyzy\pcl2.lnk')
    exit()

if select == 3:
    os.system('G:\pyzy\qq.lnk')
    exit()

if select == 4:
    os.system('G:\pyzy\ps.lnk')
    exit()

if select == 5:
    os.system('G:\pyzy\pr.lnk')
    exit()

if select == 6:
    os.system('G:\pyzy\wo18.lnk')
    exit()

if select == 7:
    print("[1] 启动 SSTap      [2] 启动 JustProxy")
    choice = int(input("↑ 输入 [] 里对应的内容进行选择 : "))
    if choice == 1:
        os.system('G:\pyzy\st.lnk')
        exit()
    if choice == 2:
        os.system('G:\pyzy\jp.lnk')
        exit()

if select == 8:
    os.system('G:\pyzy\wx.lnk')
    exit()

if select == 9:
    os.system('G:\pyzy\pl.lnk')
    exit()

if select == 10:
    os.system('G:\pyzy\dc.lnk')
    exit()

if select == 11:
    os.system('G:\pyzy\obs.lnk')
    exit()

if select == 12:
    os.system('G:\pyzy\wt.lnk')
    exit()

if select == 13:
    os.system('G:\pyzy\sz.lnk')
    exit()

if select == 14:
    os.system('G:\pyzy\pf.lnk')
    exit()

if select == 15:
    os.system('G:\pyzy\wcm.lnk')
    exit()

if select == 16:
    os.system('G:\pyzy\sc.lnk')
    exit()


if select == 17:
    os.system('G:\pyzy\dism64.lnk')
    exit()

if select == 18:
    print("CMD版菜单等待制作中")

if select == 19:
    exit()

#此菜单Made by WTP016 , 未经许可，禁止使用。
