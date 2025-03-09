#员工管理模块
import requests


class IhrmEmpCurd(object):
    #添加员工
    @classmethod
    def add_emp(cls,header,json_data):
        url = "https://ihrm-java.itheima.net/api/sys/user"
        resp_add = requests.post(url=url, headers=header, json=json_data)
        return resp_add
    #查询员工
    @classmethod
    def query_emp(cls,emp_id,header):
        query_url = "https://ihrm-java.itheima.net/api/sys/user/"+emp_id
        resp_query = requests.get(url=query_url, headers=header)
        return resp_query
    #修改员工
    @classmethod
    def update_emp(cls,emp_id,header,json_data):
        update_url = "https://ihrm-java.itheima.net/api/sys/user/"+emp_id
        resp_update = requests.put(url=update_url, headers=header, json=json_data)
        return resp_update
    #删除员工
    @classmethod
    def delete_emp(cls,emp_id,header):
        delete_url = "https://ihrm-java.itheima.net/api/sys/user/"+emp_id
        resp_delete = requests.delete(url=delete_url, headers=header)
        return resp_delete