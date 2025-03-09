import requests

#添加员工
url="https://ihrm-java.itheima.net/api/sys/user"
headers = {"Content-Type": "application/json","Authorization": "Bearer 033a3ca4-985b-4d04-b491-ad239f1dc6a0"}
json_data={
    "username": "www",
    "mobile": "15335886611",
    "workNumber":"9527"
}
resp_add=requests.post(url=url,headers=headers,json=json_data)
print("添加员工",resp_add.json())
#查询员工
query_url="https://ihrm-java.itheima.net/api/sys/user/12345676601"
query_headers = {"Content-Type": "application/json","Authorization": "Bearer 033a3ca4-985b-4d04-b491-ad239f1dc6a0"}

resp_query=requests.get(url=query_url,headers=query_headers)
print("查询员工",resp_add.json())
#修改员工
update_url="https://ihrm-java.itheima.net/api/sys/user/12345676601"
update_headers = {"Content-Type": "application/json","Authorization": "Bearer 033a3ca4-985b-4d04-b491-ad239f1dc6a0"}
update_data={
    "username": "qitiandasheng",
}
resp_update=requests.put(url=update_url,headers=update_headers,json=update_data)
print("修改员工",resp_update.json())
#删除员工
delete_url="https://ihrm-java.itheima.net/api/sys/user/12345676601"
delete_headers = {"Content-Type": "application/json","Authorization": "Bearer 033a3ca4-985b-4d04-b491-ad239f1dc6a0"}

resp_delete=requests.delete(url=delete_url,headers=delete_headers)
print("删除员工",resp_delete.json())