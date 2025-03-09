import unittest

from api.ihrm_emp_curd import IhrmEmpCurd
from common.assert_util import assert_util


class EmpAddTest(unittest.TestCase):
    #必选参数
    def test01_emp_add(self):
        headers = {"Content-Type": "application/json", "Authorization": "Bearer 033a3ca4-985b-4d04-b491-ad239f1dc6a0"}
        json_data = {
            "username": "www",
            "mobile": "15367786889",
            "workNumber": "9527"
        }
        resp=IhrmEmpCurd.add_emp(headers, json_data)
        print("必须：",resp.json())
        assert_util(self,resp, 200,True,10000,'操作成功')

    #组合参数
    def test02_emp_add(self):
        headers={
            "Content-Type": "application/json",
                   "Authorization": "Bearer 033a3ca4-985b-4d04-b491-ad239f1dc6a0"}
        json_data = {
            "username": "www",
            "mobile": "16637799889",
            "workNumber": "9527",
            "fromOfEmployment":"2"
        }
        resp=IhrmEmpCurd.add_emp(headers, json_data)
        print("组合：",resp.json())
        assert_util(self,resp, 200,True,10000,'操作成功')
    #全部参数
    def test03_emp_add(self):
        headers = { "Content-Type": "application/json",
                   "Authorization": "Bearer 033a3ca4-985b-4d04-b491-ad239f1dc6a0"}
        json_data = {
            "username": "www",
            "mobile": "16630006889",
            "workNumber": "9527",
            "fromOfEmployment": "1"
        }
        resp = IhrmEmpCurd.add_emp(headers, json_data)
        print("全部：", resp.json())
        assert_util(self, resp, 200, True, 10000, '操作成功')