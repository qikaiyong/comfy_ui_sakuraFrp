#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-05-02 19:56
# @Author  : 我的名字
# @File    : __init__.py
# @Description : 这个函数是用来balabalabala自己写
import subprocess

# 第一个命令：修改文件权限
chmod_command = ["chmod", "+x", "frpc"]
subprocess.run(chmod_command, check=True)

# 第二个命令：运行 frpc 客户端
frpc_command = ["./frpc", "-f", "azqc9s9cnc2peh75533rqpvkuef24lfm:22185092"]
subprocess.run(frpc_command, check=True)
