import sys
from cx_Freeze import setup, Executable

# 基础设置
base = None
if sys.platform == "win32":
    pass
    # base = "Win32GUI"  # 如果是 GUI 程序，使用这个设置；如果是命令行程序，将这行注释掉

# 可执行文件设置
executables = [
    Executable("add_template.py", base=base)
]

# 打包设置
setup(
    name="add_template",
    version="0.1",
    description="读取xlsx商品数据,录入网页",
    executables=executables
)