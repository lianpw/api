import unittest
from api.api_variety_list import ApiVarietyList
from parameterized import parameterized
from tools.read_json import read_json
from tools.login_and_header import LoginAndHeader


# 种类列表接口业务层实现
class TestVarietyList(unittest.TestCase):
    @parameterized.expand(read_json('variety_list.json'))
    def test_variety_list(self, url, code):
        res = ApiVarietyList().api_variety_lisg(url, LoginAndHeader().get_header())
        print(res.json())