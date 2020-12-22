# -*- coding: utf-8 -*-
import os
import unittest
import HTMLTestRunner
from test.runmethod import RunMethod


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.run = RunMethod()

    def test_异动(self):
        url = 'http://collection-aliyun1.aicaitest.com:18210/external/action/event/notify'
        data = "{\r\n    \"userId\":\"60000102\",\r\n    \"userName\":\"徐亚春\",\r\n    \"identityCard\":\"360124198911142144\",\r\n    \"userPhone\":\"18520010200\",\r\n    \"deviceNo\":\"8856695\",\r\n    \"actionType\":\"1\",\r\n    \"actionName\":\"爱又米登陆\",\r\n    \"actionTime\":\"2020-09-26 14:10:01\",\r\n    \"remarks\":\"无需重试\"  \r\n}"
        byte_data = data.encode('utf-8')
        data2={
            "userId": "60000102",
            "userName": "徐亚春",
            "identityCard": "360124198911142144",
            "userPhone": "18520010200",
            "deviceNo": "8856695",
            "actionType": "1",
            "actionName": "爱又米登陆",
            "actionTime": "2020-09-26 14:10:01",
            "remarks": "无需重试"
        }
        header = {
            'appkey': 'zmifu9k5w1',
            'appSecret': 'az9dctvfseg1cht5ff9dlwvh96mz6dgs',
            'rentCode': '0024',
            'partnerCorp': '323',
            'productType': '324',
            'timestamp': '20200921140404',
            'Content-Type': 'application/json;charset=utf-8'
        }
        res = self.run.run_main('Post', url, byte_data, header)
        self.assertIn('00000000', res, '测试不通过')

    def test_逾期查询(self):
        url = "http://collection-static-aliyun1.aicaitest.com:8000/collectionWebBackend/fq/createNetpue"
        pay_load = "{\r\n    \"userId\":80080008,\r\n    \"target\":\"2020080050228\",\r\n    \"periodNum\":1," \
                   "\r\n    \"instalmentTime\":\"Jul 10, 2020 12:00:00 AM\",\r\n    \"loanProvider\":\"qinjia\"," \
                   "\r\n    \"orderType\":202260,\r\n    \"amtCapital\":2000000,\r\n    \"unpayAmtCapital\":1515780," \
                   "\r\n    \"unpayAmtFee\":234210,\r\n    \"postItemList\":[\r\n        {\r\n            " \
                   "\"period\":1,\r\n            \"amtCapital\":162550,\r\n            \"amtService\":20000," \
                   "\r\n            \"amtManager\":11890,\r\n            \"amtFactorage\":0,\r\n            " \
                   "\"amtCoupon\":0,\r\n            \"amtOverDueFee\":0,\r\n            \"payDate\":\"Aug 30, " \
                   "2020 12:00:00 AM\",\r\n            \"postponeUpTime\":\"Aug 5, 2020 12:10:00 AM\"\r\n        " \
                   "}\r\n    ],\r\n    \"realname\":\"周佳08\",\r\n    \"idcard\":\"110101200101019952\"," \
                   "\r\n    \"telephone\":\"15888880010\",\r\n    \"sex\":\"female\",\r\n    \"createTime\":\"Jul 13, " \
                   "2020 10:47:16 AM\",\r\n    \"qq\":\"8856695\",\r\n    \"familyProvinceName\":\"浙江省\"," \
                   "\r\n    \"familyCityName\":\"杭州市\",\r\n    \"schoolName\":\"北京大学\"," \
                   "\r\n    \"familyAddress\":\"华星路96号\",\r\n    \"companyName\":\"油泼面龙总\"," \
                   "\r\n    \"companyAddress\":\"多N95与我哦哦\",\r\n    \"contactList\":[\r\n        {\"linkName\": " \
                   "\"wangwu\",\r\n\"linkTel\":\"13281111112\",\r\n\"reference\": \"father\"}\r\n\r\n    ]\r\n} "
        byte_data = pay_load.encode('utf-8')
        header = {
            'appkey': 'v4poh50d86',
            'appSecret': 'ycdyuzw267ez93is5kwnp1h0atr8hw2u',
            'rentCode': '0024',
            'partnerCorp': '323',
            'productType': '324',
            'timestamp': '2020081115300123',
            'Content-Type': 'application/json;charset=utf-8'
        }
        res = self.run.run_main('Post',url, byte_data, header)
        self.assertIn('00000000', res, '测试不通过')


if __name__ == '__main__':
    filepath = os.getcwd() + '\\report.html'
    fp = open(filepath, 'wb+')

    suite = unittest.TestSuite(unittest.makeSuite(MyTestCase))
    #suite.addTest(MyTestCase('test_yd'))


    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='米盾云接口测试')
    runner.run(suite)
    # unittest.main()
