import logging
from public.ethics_public.log import MyTestCase
import time
import unittest
import requests
import time
from public.ethics_public.ethics_login import ethics
from public.ethics_public.projectId import edproject
from unittestreport import rerun

# 获取当前时间
now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


class MyTestCase(unittest.TestCase):

    def test001subMater(self):
        """点击提交材料"""
        url = 'http://gcpmsapi.ashermed.cn/api/v3/User/GetAccountSignature?api-version=3'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
               }
        payload = {
              "personnelId": "2",
              "userId": 2
            }
        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('查询成功', print(result))
            logging.info('查询成功', result)
        else:
            self.assertFalse('查询失败', print(result))
            logging.error('查询失败', result)

    def test002saveMater(self):
        """提交伦理材料"""
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
          "projectId": edproject.rid,
          "stageId": 8,
          "createUserId": "2",
          "RightUserId": "2",
          "ethicalFileData": {
            "registrationNumber": None,
            "getDate": "2021-10-13",
            "updateCycle": "3",
            "ethicalFileDataParams": [
              {
                "fileId": 1,
                "docUrl": "[{\"name\":\"伦理正式批件\",\"id\":\"c2a69ece4ce87f2d4d296467cf738e89\",\"type\":\"image/jpeg\"}]"
              },
              {
                "fileId": 2,
                "docUrl": "[{\"name\":\"知情同意书\",\"id\":\"ff3471dcbd4ecb2d81076d3a48420dd6\",\"type\":\"image/jpeg\"}]"
              },
              {
                "fileId": 3
              },
              {
                "fileId": 5
              }
            ]
          },
          "isCompleted": True
        }
        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('提交伦理材料成功', print(result))
            logging.info('提交伦理材料成功', result)
        else:
            self.assertFalse('提交伦理材料失败', print(result))
            logging.error('提交伦理材料失败', result)

    def test003manMater(self):
        """人遗调查表提交"""
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
          "projectId": edproject.rid,
          "stageId": 10,
          "questionnaireParam": {
            "projectName": None,
            "ethicsNumber": "测试110123",
            "projectSource": "来源未知",
            "sponsor": "瑞金医院",
            "leaderUnit": "瑞金医院",
            "department": "超声科",
            "researchers": "张慧霞",
            "basicSituation1": "1",
            "basicSituation2": "1",
            "basicSituation3": "1",
            "isMaterialAcquisition": "0",
            "materialAcquisition1": "",
            "materialAcquisition2": "",
            "materialAcquisition3A": "",
            "materialAcquisition3B": "",
            "isInfoCollection": "",
            "infoCollection1": "",
            "infoCollection2": "",
            "infoCollection3A": "",
            "infoCollection3B": "",
            "preservationResources1": "1",
            "preservationResources2": "1",
            "scientificResearch1": "0",
            "scientificResearch2": "",
            "scientificResearch3": "",
            "scientificResearch4": "",
            "scientificResearch5": "0",
            "scientificResearch6": "",
            "scientificResearch7": "",
            "geneticResourcesExit": "0",
            "offeredOrOpenUse": "0",
            "ethicalFileData": []
          },
          "isCompleted": False
        }
        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('人遗调查表提交成功', print(result))
            logging.info('人遗调查表提交成功', result)
        else:
            self.assertFalse('人遗调查表提交失败', print(result))
            logging.error('人遗调查表提交失败', result)

    def test004badMater(self):
        """临床研究网站注册提交"""
        url = 'http://gcpmsapi.ashermed.cn/api/Project/save'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'}
        payload = {
          "projectId": edproject.rid,
          "stageId": 11,
          "clinicalResearchWebsite": [
            {
              "registrationNumber": "yb1213123123",
              "registryPlatform": "瑞金"
            }
          ],
          "isCompleted": True
        }
        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('临床研究网站注册提交成功', print(result))
            logging.info('临床研究网站注册提交成功', result)
        else:
            self.assertFalse('临床研究网站注册提交失败', print(result))
            logging.error('临床研究网站注册提交失败', result)

    def test005smMater(self):
        """提交申请材料"""
        url = 'http://gcpmsapi.ashermed.cn/api/Project/submit'
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
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('提交申请材料成功', print(result))
            logging.info('提交申请材料成功', result)
        else:
            self.assertFalse('提交申请材料失败', print(result))
            logging.error('提交申请材料失败', result)

    def test006saMater(self):
        """保存伦理批件"""
        url = 'http://gcpmsapi.ashermed.cn/api/ProjectReport/SaveReportRecord'
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
              "recordCategory": "7",
              "files": "[{\"name\":\"ff.jpg\",\"type\":\"image/jpeg\",\"id\":\"ff3471dcbd4ecb2d81076d3a48420dd6\"}]",
              "getDate": now_time,
              "operatorId": "2",
              "userName": "张慧36",
              "parentRecordId": None
            }
        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('保存伦理批件成功', print(result))
            logging.info('保存伦理批件成功', result)
        else:
            self.assertFalse('保存伦理批件失败', print(result))
            logging.error('保存伦理批件失败', result)

    # def test007smsMater(self):
    #     """伦理递交记录提交"""
    #     url = 'http://gcpmsapi.ashermed.cn/api/ProjectReport/SubmitReportRecord'
    #     headers = {
    #         'Token': ethics.token,
    #         'ClientType': '1',
    #         'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
    #         'Content-Type': 'application/json;charset=UTF-8',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                       'Chrome/92.0.4515.107 Safari/537.36'
    #         }
    #     payload = {
    #           "projectId": edproject.rid,
    #           "recordCategory": "7",
    #           "files": "[{\"name\":\"ff.jpg\",\"type\":\"image/jpeg\",\"id\":\"ff3471dcbd4ecb2d81076d3a48420dd6\"}]",
    #           "operatorId": "2",
    #           "parentRecordId": 0
    #         }
    #     result = requests.post(url=url, headers=headers, json=payload)
    #     result = result.json()
    #     detailedStatus = result["detailedStatus"]
    #     if detailedStatus == 1:
    #         self.assertTrue('伦理递交记录提交成功', print(result))
    #         logging.info('伦理递交记录提交成功', result)
    #     else:
    #         self.assertFalse('伦理递交记录提交失败', print(result))
    #         logging.error('伦理递交记录提交失败', result)

    def test008shMater(self):
        """人遗调查表审核"""
        url = 'http://gcpmsapi.ashermed.cn/api/Project/Ethical/GeneticApproval'
        headers = {
            'Token': ethics.token,
            'ClientType': '1',
            'ClientId': '5ad5b1b17dcc44ba5e15788b087ceea1',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.107 Safari/537.36'
        }
        payload ={
              "projectId": edproject.rid,
              "resourceApprovalFiling": "2",
              "auditStatus": 1,
              "auditType": 1
            }
        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('人遗调查表审核成功', print(result))
            logging.info('人遗调查表审核成功', result)
        else:
            self.assertFalse('人遗调查表审核失败', print(result))
            logging.error('人遗调查表审核失败', result)

    def test009shMater(self):
        """确认立项"""
        url = 'http://gcpmsapi.ashermed.cn/api/Project/Confirm'
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
              "status": 1,
              "reason": "",
              "userRole": "科研处-形式审查,科研处-立项确认,学术专家,人遗审查,科研处,学术专家-快审,科研处-报告审查,科研处-账号管理,学术审查,方法学管理,研究者,科技处负责人,成果转化办公室",
              "projectEndTime": "2021-10",
              "projectStartTime": "2021-12",
              "dateNoTermination": 0
            }
        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('确认立项成功', print(result))
            logging.info('确认立项成功', result)
        else:
            self.assertFalse('确认立项失败', print(result))
            logging.error('确认立项失败', result)

    def test010detMater(self):
        """删除项目数据"""
        url = 'http://gcpmsapi.ashermed.cn/api/Project/delete'
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
            "userId": "2"
              }
        result = requests.post(url=url, headers=headers, json=payload)
        result = result.json()
        detailedStatus = result["detailedStatus"]
        if detailedStatus == 1:
            self.assertTrue('删除项目成功', print(result))
            logging.info('删除项目成功', result)
        else:
            self.assertFalse('删除项目失败', print(result))
            logging.error('删除项目失败', result)


if __name__ == '__main__':
    unittest.main()
