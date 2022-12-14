import ctypes
import datetime
import os
import sys

dt = datetime.datetime.now()

cwd = os.getcwd()
STD_OUTPUT_HANDLE = -11


class CONSTS:
    TRANS_KW_DICTS = {
        "导入 ": "import ",
        "否则如果 ": "elif ",
        "如果 ": "if ",
        "否则": "else ",
        "定义": "def",
    }
    TRANS_SN_DICTS = {
        "打印": "print",
        "从控制台获取输入 ": "input ",
        "获取输入": "input",
        "（": "(",
        "）": ")",
        "”": "\"",
        "“": "\"",
        "：": ":",
        "、": "\\",
        "‘": "\'",
        "《": "<",
        "》": ">",
        "，": ",",
        "。": ".",
        "【": "[",
        "】": "]",
        "÷": "/",
        "×": "*",
        "！": "!",
        "￥": "$",
        "……": "^",
        "——": "_",
        "系统": "os",
        "绘图": "turtle",
        "GUI": "easygui",
        "图形化用户界面": "easygui",
        "转换为整数": "int",
        "整数": "int",
        "转换为字符串": "str",
        "字符串": "str",
        "转换为布尔值": "bool",
        "布尔值": "bool",
        "真": "True",
        "假": "False",
        "hz-": "#",
        "kz-": "\"\"\"",
        "-kz": "\"\"\"",
    }
    import os
    TRANS_PATH = f"{os.getenv('USERPROFILE')}\\Temp\\Local\\Py-CN\\"
    TRANS_FILE_NAME = "PCNP_output.py"


class Modes:
    INFO = "INFO"
    WARN = "WARN"
    ERR = "ERROR"
    FATAL = "FATAL"
    DEBUG = "DEBUG"


class Ports:
    CLIENT = "Client"
    SERVER = "Server"
    COMMON = "Server"
    DOWN = "Downloading"
    TH = "Threading"


class Utils:
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    BLUE = 0x09
    GREEN = 0x0a
    RED = 0x0c
    YELLOW = 0x0e

    # noinspection PyBroadException
    @staticmethod
    def log(data: str, mode: str = Modes.INFO, port: str = Ports.CLIENT):
        willBeWritenData: str = f"[{dt.strftime('%Y-%m-%d %H:%M:%S:') + str(datetime.datetime.now().microsecond)}] [{port}|{mode}] {data} \n"
        isExists: bool
        # noinspection PyBroadException
        try:
            with open(f"{cwd}\\logs\\{dt.strftime('%Y-%m-%d')}_run.log", "r+") as f:
                if "Stopping!" in f.read():
                    isExists = True
                else:
                    isExists = False
        except:
            isExists = False
        if isExists:
            with open(f"{cwd}\\logs\\{dt.strftime('%Y-%m-%d')}_run.log", "w") as f:
                f.write("")
            with open(f"{cwd}\\logs\\{dt.strftime('%Y-%m-%d')}_run.log", "a+") as f:
                f.write(willBeWritenData)
        else:
            with open(f"{cwd}\\logs\\{dt.strftime('%Y-%m-%d')}_run.log", "a+") as f:
                f.write(willBeWritenData)
        with open(f"{cwd}\\logs\\{dt.strftime('%Y-%m-%d')}_run.log", "a+") as f:
            f.write(
                f"[{dt.strftime('%Y-%m-%d %H:%M:%S:') + str(datetime.datetime.now().microsecond)}] [{port}|{mode}] Stopping! \n")

    @staticmethod
    def printColor(welcomeText: str, color: hex) -> None:
        Utils.setColor(Utils.std_out_handle, color)
        sys.stdout.write(welcomeText)
        print()

    @staticmethod
    def setColor(__std_out_handle, color) -> None:
        return ctypes.windll.kernel32.SetConsoleTextAttribute(__std_out_handle, color)


def translate(args: str) -> str:
    for k, v in (CONSTS.TRANS_SN_DICTS | CONSTS.TRANS_KW_DICTS).items():
        args = args.replace(k, v)
    return args


# noinspection PyBroadException
def findPyFile(file: str) -> bool:
    if file != "":
        # noinspection PyBroadException
        try:
            with open(f"{CONSTS.TRANS_PATH}py-cn.tmp", "a+") as f:
                f.write("Py-CN Test File")
            Utils.log(f"Created test file in {CONSTS.TRANS_PATH}.", Modes.INFO)
        except:
            Utils.log(f"CANNOT create test file in {CONSTS.TRANS_PATH}, and it will be ignored.", Modes.WARN)
        try:
            with open(file, "r"):
                Utils.log(f"Found file in {CONSTS.TRANS_PATH}.", Modes.INFO)
            return True
        except Exception as e:
            Utils.log(f"CANNOT find file in {CONSTS.TRANS_PATH}!", Modes.ERR)
            Utils.log(f"The following information is received: {e.__doc__}")
            Utils.log(e.__str__(), Modes.ERR)
        return False


def findFile(file: str) -> bool:
    try:
        with open(file, "r") as f:
            Utils.log(f"Found file in {f.name}.", Modes.INFO)
        return True
    except Exception as e:
        Utils.log(f"CANNOT find file!", Modes.ERR)
        Utils.log(f"The following information is received: {e.__doc__}", Modes.ERR)
        Utils.log(e.__str__(), Modes.ERR)
    return False


def readFile(file: str) -> str | int:
    # try:
    with open(file, "r", encoding="utf-8") as f:
        Utils.log(f"Found file in {f.name}.", Modes.INFO)
        return f.read()


# except Exception as e:
#     Utils.log(f"CANNOT find file!", Modes.ERR)
#     Utils.log(f"The following information is received: {e.__doc__}", Modes.ERR)
#     Utils.log(e.__str__(), Modes.ERR)
#     return "错误"


# noinspection PyGlobalUndefined
def compileFile(file: str) -> str:
    # noinspection PyGlobalUndefined
    global content
    content = ""
    try:
        with open(file, "r+", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError as e:
        Utils.log(f"CANNOT find file!", Modes.ERR)
        Utils.log(f"The following information is received: {e.__doc__}", Modes.ERR)
        Utils.log(e.__str__(), Modes.ERR)
    except Exception as e:
        Utils.log(f"There was a/many problem(s) was/were thrown!", Modes.ERR)
        Utils.log(f"The following information is received: {e.__doc__}", Modes.ERR)
        Utils.log(e.__str__(), Modes.ERR)
    return "#-*- coding: utf-8 -*-\n" + translate(content)


def saveFile(contents: str, file: str):
    try:
        with open(file, "w", encoding="utf-8") as f:
            f.write(contents)
    except Exception as e:
        Utils.log(f"There was a/many problem(s) was/were thrown!", Modes.ERR)
        Utils.log(f"The following information is received: {e.__doc__}", Modes.ERR)
        Utils.log(e.__str__(), Modes.ERR)


def hasPythonOrLowerThanRequired():
    import sys

    if sys.version_info < (0, 0):
        print("未检测到 Python，请下载 Python！")
    elif sys.version_info < (3, 10):
        print("至少需要 Python 3.10！")
    else:
        return None
    choice = input("输入 X 或 P 下载 Python 3.10.7（可能很慢）；输入 A 或 I 安装 Python 3.10.7；不输入或输入 E 退出程序！")

    if choice.__eq__("X") | choice.__eq__("P"):
        import urllib.request as ur
        ur.urlretrieve("https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe", "python-3.10.7-amd64.exe")
        os.system("start .\\\"python-3.10.7-amd64.exe\"")
    elif choice.__eq__("A") | choice.__eq__("I"):
        os.system("start .\\\"python-3.10.7-amd64.exe\"")
    else:
        if choice.__eq__("E") or choice is None or choice == "":
            exit()
        else:
            hasPythonOrLowerThanRequired()


def easterEgg():
    month = dt.now().month
    day = dt.now().day
    if (month == 10 and day == 1) or (month == 9 and day == 30):
        Utils.printColor(
            "\n===HAPPY================================= 国庆节快乐! ===========NATIONAL===============DAY==\n",
            Utils.RED)
        #Utils.printColor("========================================= 国庆节快乐! =========================================", Utils.RED)