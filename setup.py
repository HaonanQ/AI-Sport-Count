# -*- coding:utf-8 -*-
# author: cyz
# time: 2021/9/22 9:35
import os, sys
# is ok
from cx_Freeze import setup, Executable

# 隐藏控制台
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

# 主运行程序
executables = [Executable("main.py", base=base,icon="icon.ico")]
# 需要引用的第三方包
packages = ["jupyter","mediapipe","numpy","pandas","ttkbootstrap"]
excludes =[]
# 排除不压缩进去
# 需要额外的数据文件
include_files = ["F:\AImo\Sport-With-AI-main\images\scoretable.png"] + ["bodypartangle.py","typesofexercise.py","utils.py","keepsport.py"]  # 把自定义包作为外部数据文件


options = {
    'build_exe': {
        'packages':packages,
        'include_files':include_files,
        'excludes':excludes
    },
}

setup(
    name = "AI教练",  # 应用名称
    options = options,
    version = "2.3.4989",  # 版本号
    description = '智能检查运动情况',  # 描述
    executables = executables
)
