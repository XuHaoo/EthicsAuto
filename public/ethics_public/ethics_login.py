# -*- coding:utf-8 -*-
import logging
import unittest
import requests
import time
from public.ethics_public import host


def __init__(self, requests):
    self.requests = requests  # 设置全局参数


class ethics:

    def login(self, token):
        """登录获取token等信息"""
        self.Token = token

    # 登录URL地址信息
    url_login = host + '/v3/Login/SingleSignOnByLoginId?api-version=3'
    # body参数信息
    payload = {
        "loginId": "13681899297",
        "loginPwd": "899297",
        "isExclusiveLogin": True,
        "clientId": "5ad5b1b17dcc44ba5e15788b087ceea1",
        "clientType": 1
    }
    result = requests.post(url_login, json=payload)
    logging.info(payload)
    result = result.json()
    print(result)
    token = result["data"]["token"]
    # 判断返回结果是否正确
    detailedStatus = result["detailedStatus"]
    if detailedStatus == 1:
        print('登录成功Token:', token)
    else:
        print('登录错误')


if __name__ == '__main__':
    unittest.main()
