import requests


# 种类列表接口对象层封装
class ApiVarietyList:
    def api_variety_lisg(self, url, header):
        return requests.get(url, headers=header)