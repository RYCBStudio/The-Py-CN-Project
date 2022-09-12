"""
Copyright <c> 2022 RYCBStudio, all rights reserved.
"""

import utils
import os

if __name__ == '__main__':
    print("======================================== Welcome To  ========================================")
    print(r""" _____ _             ______                 _____  _   _     ______          _           _   
|_   _| |            | ___ \               /  __ \| \ | |    | ___ \        (_)         | |  
  | | | |__   ___    | |_/ /   _   ______  | /  \/|  \| |    | |_/ / __ ___  _  ___  ___| |_ 
  | | | '_ \ / _ \   |  __/ | | | |______| | |    | . ` |    |  __/ '__/ _ \| |/ _ \/ __| __|
  | | | | | |  __/   | |  | |_| |          | \__/\| |\  |    | |  | | | (_) | |  __/ (__| |_ 
  \_/ |_| |_|\___|   \_|   \__, |           \____/\_| \_/    \_|  |_|  \___/| |\___|\___|\__|
                            __/ |                                          _/ |              
                           |___/                                          |__/               """)
    print("========================================= Ver 0.0.1 =========================================")
    file = input("请输入文件名：")
    print("正在寻找文件...")
    utils.Utils.log("Finding the Py-cn files")
    if utils.findFile(".\\" + file + ".pycn"):
        print("找到文件！")
        print(f"文件路径为：{os.getcwd()}\\{file}.pycn")
        print(f"文件内容为：\n{utils.readFile('./' + file + '.pycn')}")
        print("编译中...")
        utils.saveFile(utils.compileFile('./' + file + '.pycn'), f".\\{'./' + file}.py")
        print("运行中...")
        print("[--------- The Py-CN Project Console ---------]")
        print(f">> $Run(\"{file + '.pycn'}\")")
        print(f"========== Start Program: \"{file + '.pycn'}\" ==========")
        os.system("python " + ".\\" + file + ".py")
        print("================= End Program =================")
    else:
        file = input("未找到文件，请输入您的文件完整路径：(比如：C:\\xxx.pycn)")
        if utils.findFile(file):
            print("找到文件！")
            print(f"文件路径为：{file}")
            print(f"文件内容为：\n{utils.readFile(file)}")
            print("编译中...")
            utils.saveFile(utils.compileFile(file), f".\\{file}.py")
            print("[--------- The Py-CN Project Console ---------]")
            print(f">> $Run(\"{file + '.pycn'}\")")
            print(f"========== Start Program: \"{file + '.pycn'}\" ==========")
            os.system("python " + file)
            print("================= End Program =================")
        else:
            print("未找到文件！")
