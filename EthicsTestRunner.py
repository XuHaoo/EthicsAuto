from reports import HTMLTestRunner
from TestRunner import HTMLTestRunner
import unittest
import os
import time
from case.project_case.addproject_case import Addprojectcase
from case.project_case.submitMaterial import MyTestCase
from TestRunner import SMTP

# 创建测试套件
suite = unittest.TestSuite()

# 添加多个测试用例

# 新增项目测试用例
suite.addTests([Addprojectcase("test001_addprojectcase"),
                Addprojectcase("test002_addprojectcase"),
                Addprojectcase("test003_addprojectcase"),
                Addprojectcase("test004_addprojectcase"),
                Addprojectcase("test005_addprojectcase"),
                Addprojectcase("test006_addprojectcase"),
                Addprojectcase("test007_addprojectcase"),
                Addprojectcase("test008_addprojectcase"),
                Addprojectcase("test009_addprojectcase"),
                Addprojectcase("test010_addprojectcase"),
                Addprojectcase("test011_addprojectcase"),
                Addprojectcase("test012_addprojectcase"),
                Addprojectcase("test013_addprojectcase"),
                Addprojectcase("test014_addprojectcase"),
                Addprojectcase("test015_addprojectcase"),
                Addprojectcase("test016_addprojectcase")
              # Addprojectcase("test017_addprojectcase"),
                ])
# 项目资料完善
suite.addTests([MyTestCase("test001subMater"),
                MyTestCase("test002saveMater"),
                MyTestCase("test003manMater"),
                MyTestCase("test004badMater"),
                MyTestCase("test005smMater"),
                MyTestCase("test006saMater"),
                MyTestCase("test008shMater"),
                MyTestCase("test009shMater"),
              # MyTestCase("test010detHist"),
                MyTestCase("test011detStop"),
                MyTestCase("test012detStopAudit"),
                MyTestCase("test013detRest"),
                MyTestCase("test014detRestAudit"),
                MyTestCase("test015detSuspend"),
                MyTestCase("test016detSuspendAudit"),
                MyTestCase("test020detMater")
                ])

#
# # 定义测试报告的存放的路径
# path = r"D:\Desktop\reports"
# # 判断路径是否存在
# if not os.path.exists(path):
#     # 如果不存在，则创建一个
#     os.makedirs(path)
# else:
#     pass
# # 定义一个时间戳用于测试报告命名
# now_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
# reports_path = path + "\\" + now_time + "(exam_report).html"
# reports_title = u"伦理系统——测试报告"
# desc = u"伦理系统——接口自动化测试报告"
# # 二进制写
# fp = open(reports_path, "wb")
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=reports_title, description=desc)
# # 运行
# # runner.run(suite)

# 新版测试报告，包含测试用例重试机制、日志
report = "./result.html"
with(open(report, 'wb')) as fp:
    runner = HTMLTestRunner(stream=fp,title='伦理系统接口自动化测试报告')
    """
    suit ： 运行的测试套件
    rerun ：重跑次数，设置为2，会在用例失败/错误后进行两次重试。
    save_last_run ：是否保存最后一个结果
    """
    runner.run(suite, rerun=2, save_last_run=False)
    """
    SMTP类说明：
    user 发送者邮箱帐号
    password 发送者邮箱密码
    host 邮箱服务器地址
    sender()方法说明：
    to 接收者邮箱
    attachments 附件
    """
    # # 发邮件功能
    smtp = SMTP(user="2445955870@qq.com", password="uezqtcwexllveaii", host="smtp.qq.com")
    smtp.sender(to="test@ashermed.com", attachments=report)
