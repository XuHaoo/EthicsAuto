import time
import unittest
import requests
from public.ethics_public.ethics_login import ethics


def __init__(self, requests):
    self.requests = requests  # 设置全局参数


class edproject:

    def projectcase(self, rid):
        """新增项目--项目概况表信息"""
        self.rid = rid

    # 获取当前时间
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    url = 'http://gcpmsapi.ashermed.cn/api/Project/save'
    headers = {
        'Token': ethics.token,
        'ClientType': '1',
        'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.107 Safari/537.36'
    }
    payload = {
        "projectId": None,
        "stageId": 1,
        "basicData": {
            "name": "自动化测试进行Test" + now_time,
            "applicant": "张慧霞",
            "department": "37",
            "departmentName": "超声科",
            "contactPerson": "测测",
            "contactInfo": "13671679931",
            "sampleSize": 111,
            "indicationRange": 2,
            "researchType": 1,
            "researchRisk": 1,
            "isApprovedProject": 1,
            "globalCooperation": 1,
            "fundingSource": 1,
            "participationWay": 1,
            "researchFundingType": 1,
            "sourceTopics": "测试",
            "projectTime": "2021-10-11",
            "leadUnit": "侧是是是",
            "sponsor": "",
            "contactEmail": "hao.xu@ashermed.com",
            "ifTheStarting": 1
        },
        "isCompleted": True
    }
    result = requests.post(url, json=payload, headers=headers)
    result = result.json()
    print(result)
    # 添加一个ProjectID为其他用例调用
    rid = result["data"]
    globals()["data"] = rid
    print(rid)
    detailedStatus = result["detailedStatus"]
    if detailedStatus == 1:
        # self.assertTrue('添加项目概况成功', result)
        print('添加项目概况成功', result)
    else:
        # self.assertFalse('添加项目概况失败', result)
        print('添加项目概况失败', result)


if __name__ == '__main__':
    unittest.main()
