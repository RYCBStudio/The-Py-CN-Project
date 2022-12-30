# -*- coding: utf-8 -*-
"""
Used for the Py-CN Project,
Copyright <c> 2022 RYCBStudio.
"""
import os

字符串 = str


def 获取系统变量所在路径(环境变量名: 字符串) -> 字符串:
    return os.getenv(环境变量名)


def 获取工作路径() -> 字符串:
    return os.getcwd()
