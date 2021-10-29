import logging
import time
import unittest
import requests
from public.ethics_public.ethics_login import ethics
from public.ethics_public.projectId import edproject
from public.ethics_public import host
# from unittestreport import rerun


class Addprojectcase(unittest.TestCase):
    """项目测试"""

    def test001_addprojectcase(self):
        """新增项目--项目概况表信息"""
        # 获取当前时间
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        url = host + '/Project/save'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
            "projectId": edproject.rid,
            "stageId": 1,
            "basicData": {
                "name": "自动化测试进行Test"+now_time,
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
        logging.info(payload)
        result = requests.post(url, json=payload, headers=headers)
        logging.info(result)
        result = result.json()
        # print(result)
        # # 添加一个ProjectID为其他用例调用
        # rid = result["data"]
        # globals()["data"] = rid
        # print(rid)
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('添加项目概况成功', print(result))
        else:
            self.assertFalse('添加项目概况失败', print(result))

    def test002_addprojectcase(self):
        """添加研究者履历"""
        url = host + '/Project/save'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
            "projectId": edproject.rid,
            "stageId": 6,
            "resumeData": {
                "name": "张慧",
                "professionalField": "内科",
                "sex": 2,
                "birthday": "2020-12-31",
                "education": "硕士",
                "position": "正高",
                "contactNumber": "13681899297",
                "phoneNumber": "13681899297",
                "email": "976360862@qq.com",
                "workExperience": "嗯嗯ee",
                "introduction": None,
                "educationExperienceParams": [
                    {
                        "startTime": "2021-01",
                        "endTime": "2021-08",
                        "school": "上海2",
                        "major": "护理",
                        "bachelorScience": "本科"
                    }
                ],
                "gcpParams": [
                    {
                        "id": 0,
                        "trainingTime": "2021-10",
                        "expirationDate": "2021-10-11",
                        "trainingName": "ces ",
                        "certificate": "{\"name\":\"cc.jpg\",\"id\":\"03cea017f0c0d5c214c8363012937b56\","
                                       "\"type\":\"image/jpeg\"} "
                    }
                ]
            },
            "isCompleted": True
        }
        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        # 判断返回结果
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('添加研究者履历成功', print(result))
        else:
            self.assertFalse('添加研究者履历失败', print(result))

    def test003_addprojectcase(self):
        """ 新增文件信息"""
        url = host + '/Project/save'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
            "projectId": edproject.rid,
            "stageId": 4,
            "createUserId": "2",
            "RightUserId": "2",
            "fileData": [
                {
                    "fileId": 1,
                    "docUrl": "[{\"name\":\"临床研究项目申请书\",\"id\":\"a0fe0ababf7a83faecea7af05580e7cd\","
                              "\"type\":\"image/png\"}] "
                },
                {
                    "fileId": 2,
                    "docUrl": "[{\"name\":\"知情同意书\",\"id\":\"c2a69ece4ce87f2d4d296467cf738e89\",\"type\":\"image/jpeg\"}]"
                }
            ],
            "isCompleted": True
        }

        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        # 判断返回结果
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('新增文件信息成功', print(result))
        else:
            self.assertFalse('新增文件信息失败', print(result))

    def test004_addprojectcase(self):
        """合作单位"""
        url = host + '/Project/save'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
            "projectId": edproject.rid, # globals()["data"]
            "stageId": 3,
            "unitData": [
                {
                    "companyName": "234234324324",
                    "pi": None,
                    "unitType": 1
                },
                {
                    "myselfId": "2007c880-2b03-11ec-96d0-15ae9a0037c5",
                    "companyName": "",
                    "pi": "",
                    "unitType": 2
                },
                {
                    "myselfId": "2007c881-2b03-11ec-96d0-15ae9a0037c5",
                    "companyName": "",
                    "pi": "",
                    "unitType": 2
                },
                {
                    "myselfId": "2007c882-2b03-11ec-96d0-15ae9a0037c5",
                    "companyName": "",
                    "pi": "",
                    "unitType": 2
                }
            ],
            "isCompleted": True
        }
        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        # 判断返回结果
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('新增合作单位成功', print(result))
        else:
            self.assertFalse('新增合作单位失败', print(result))

    def test005_addprojectcase(self):
        """提交申请"""
        url = host + '/Project/submit'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
            "projectId": edproject.rid,
            "userId": "2",
            "userName": "张慧36",
            "userRole": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室"
        }

        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        # 判断返回结果
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('提交申请失败', print(result))
        else:
            self.assertFalse('提交申请失败', print(result))

    def test006_addprojectcase(self):
        """项目概况表审核"""
        url = host +  '/Project/ResearchAudit'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
            "projectId": edproject.rid,
            "stageName": "项目概况表",
            "roleName": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室",
            "stageId": 1,
            "fileId": "",
            "status": 1,
            "reason": "",
            "userId": "2",
            "userName": "张慧36"
        }
        result = requests.post(url, headers=headers, json=payload)
        result = result.json()
        logging.info(result)
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('项目概况表审核成功', print(result))
        else:
            self.assertFalse('项目概况表审核失败', print(result))

    def test007_addprojectcase(self):
        """项目概况表审核重置"""
        url = host + '/Project/ResearchAudit'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
            "projectId": edproject.rid,
            "stageName": "项目概况表",
            "roleName": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室",
            "stageId": 1,
            "fileId": "",
            "status": 0,
            "reason": "",
            "userId": "2",
            "userName": "张慧36"
        }
        result = requests.post(url, headers=headers, json=payload)
        result = result.json()
        logging.info(result)
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('项目概况表审核重置成功', print(result))
            logging.info('项目概况表审核重置成功', result)
        else:
            self.assertFalse('项目概况表审核重置失败', print(result))
            logging.error('项目概况表审核重置失败', result)

    def test008_addprojectcase(self):
        """合作单位审核"""
        url = host + '/Project/ResearchAudit'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
            "projectId": edproject.rid,
            "stageName": "合作单位",
            "roleName": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室",
            "stageId": 3,
            "fileId": "",
            "status": 1,
            "reason": "",
            "userId": "2",
            "userName": "张慧36"
              }
        result = requests.post(url, headers=headers, json=payload)
        result = result.json()
        logging.info(result)
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('项目概况表审核重置成功', print(result))
            logging.info('合作单位审核成功', result)
        else:
            self.assertFalse('项目概况表审核重置失败', print(result))
            logging.error('合作单位审核失败', result)

    def test009_addprojectcase(self):
        """合作单位审核重置"""
        url = host + '/Project/ResearchAudit'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
              "projectId": edproject.rid,
              "stageName": "合作单位",
              "roleName": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室",
              "stageId": 3,
              "fileId": "",
              "status": 0,
              "reason": "",
              "userId": "2",
              "userName": "张慧36"
            }
        result = requests.post(url, headers=headers, json=payload)
        result = result.json()
        logging.info(result)
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('项目概况表审核重置成功', print(result))
            logging.info('合作单位审核重置成功', result)
        else:
            self.assertFalse('项目概况表审核重置失败', print(result))
            logging.error('合作单位审核重置失败', result)

    def test010_addprojectcase(self):
        """研究者履历表审核"""
        url = host + '/Project/ResearchAudit'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
          "projectId": edproject.rid,
          "stageName": "研究者履历表",
          "roleName": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室",
          "stageId": 6,
          "fileId": "",
          "status": 1,
          "reason": "",
          "userId": "2",
          "userName": "张慧36"
                }
        result = requests.post(url, headers=headers, json=payload)
        result = result.json()
        logging.info(result)
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('研究者履历表审核成功', print())
            logging.info('研究者履历表审核成功', result)
        else:
            self.assertFalse('研究者履历表审核失败', print(result))
            logging.error('研究者履历表审核失败', result)

    def test011_addprojectcase(self):
        """研究者履历表审核重置"""
        url = host + '/Project/ResearchAudit'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
          "projectId": edproject.rid,
          "stageName": "研究者履历表",
          "roleName": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室",
          "stageId": 6,
          "fileId": "",
          "status": 0,
          "reason": "",
          "userId": "2",
          "userName": "张慧36"
        }
        result = requests.post(url, headers=headers, json=payload)
        result = result.json()
        logging.info(result)
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('研究者履历表审核重置成功', print(result))
            logging.info('研究者履历表审核重置成功', result)
        else:
            print()
            self.assertFalse('研究者履历表审核重置失败', print(result))
            logging.error('研究者履历表审核重置失败', result)

    def test012_addprojectcase(self):
        """临床研究项目申请书"""
        url = host + '/Project/ResearchAudit'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
             }
        payload = {
          "projectId": edproject.rid,
          "stageName": "文件信息",
          "roleName": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室",
          "stageId": 4,
          "fileId": 1,
          "status": 1,
          "reason": "",
          "userId": "2",
          "userName": "张慧36"
            }
        result = requests.post(url, headers=headers, json=payload)
        result = result.json()
        logging.info(result)
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('临床研究项目申请书成功', print(result))
            logging.info('临床研究项目申请书成功', result)
        else:
            self.assertFalse('临床研究项目申请书失败', print(result))
            logging.error('临床研究项目申请书失败', result)

    def test013_addprojectcase(self):
        """知情同意书添加意见"""
        url = host + '/Project/ResearchAudit'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
              "projectId": edproject.rid,
              "stageName": "文件信息",
              "roleName": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室",
              "stageId": 4,
              "fileId": 2,
              "status": 3,
              "reason": "测试添加意见",
              "userId": "2",
              "userName": "张慧36"
            }
        result = requests.post(url, headers=headers, json=payload)
        result = result.json()
        logging.info(result)
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('知情同意书添加意见成功', print(result))
            logging.info('知情同意书添加意见成功', result)
        else:
            self.assertFalse('知情同意书添加意见失败', print(result))
            logging.error('知情同意书添加意见失败', result)

    def test014_addprojectcase(self):
        """知情同意书审核重置"""
        url = host + '/Project/ResearchAudit'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
            "projectId": edproject.rid,
            "stageName": "文件信息",
            "roleName": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室",
            "stageId": 4,
            "fileId": 2,
            "status": 0,
            "reason": "",
            "userId": "2",
            "userName": "张慧36"
        }
        result = requests.post(url, headers=headers, json=payload)
        result = result.json()
        logging.info(result)
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('知情同意书审核重置成功', print(result))
            logging.info('知情同意书审核重置成功', result)
        else:
            self.assertFalse('知情同意书审核重置失败', print(result))
            logging.error('知情同意书审核重置失败', result)

    def test015_addprojectcase(self):
        """知情同意书审核"""
        url = host + '/Project/ResearchAudit'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
          "projectId": edproject.rid,
          "stageName": "文件信息",
          "roleName": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室",
          "stageId": 4,
          "fileId": 2,
          "status": 1,
          "reason": "",
          "userId": "2",
          "userName": "张慧36"
        }
        result = requests.post(url, headers=headers, json=payload)
        result = result.json()
        logging.info(result)
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('知情同意书审核成功', print(result))
            logging.info('知情同意书审核成功', result)
        else:
            self.assertFalse('知情同意书审核失败', print(result))
            logging.error('知情同意书审核失败', result)

    def test016_addprojectcase(self):
        """一键通过审核"""
        url = host + '/Project/OneClickPass'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload = {
          "projectId": edproject.rid,
          "userId": "2",
          "avatar": "",
          "userName": "张慧36",
          "userRole": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室"
        }
        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('知情同意书审核成功', print(result))
            logging.info('知情同意书审核成功', result)
        else:
            self.assertFalse('知情同意书审核失败', print(result))
            logging.error('知情同意书审核失败', result)
        # try:
        #     print('成功')
        # except IOError:
        #     print(result)

    # count：用来指定用例失败重运行的次数
    # interval：指定每次重运行的时间间隔
    # 引入from unittestreport import rerun
    # 缺点是每个方法都需要进行引入
    # @rerun(count=3,interval=2)
    # def test017_addprojectcase(self):
    #     """临床研究合同书审核"""
    #     url = host + '/Project/ResearchAudit'
    #     headers = {
    #         'Token': ethics.token,
    #         'ClientType': '1',
    #         'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
    #         'Content-Type': 'application/json;charset=UTF-8',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                       'Chrome/92.0.4515.107 Safari/537.36'
    #     }
    #     payload ={
    #           "projectId": edproject.rid,
    #           "stageName": "文件信息",
    #           "roleName": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室",
    #           "stageId": 4,
    #           "fileId": 3,
    #           "status": 1,
    #           "reason": "",
    #           "userId": "2",
    #           "userName": "张慧36"
    #         }
    #     result = requests.post(url=url, headers=headers, json=payload)
    #     result = result.json()
    #     detailedStatus = result["detailedStatus"]
    #     if detailedStatus == 1:
    #         self.assertTrue('临床研究合同书审核成功',print(result))
    #     else:
    #         # self.assertFalse 此关键字HtmlTestRunner识别Fail
    #         self.assertFalse('临床研究合同书审核失败',print(result))


if __name__ == '__main__':
    unittest.main()
