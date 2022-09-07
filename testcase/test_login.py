
import pytest
import allure
import requests
from common.baseAPI import BaseAPI
from utils.handle_excel import get_excel_data
from libs.login import Login
from common.apiAssert import ApiAssert

class TestLogin:
    @pytest.mark.parametrize('title,req_body,exp_resp',get_excel_data('登录模块','Login',run_case=['003','005']))
    def test_login(self,title,req_body,exp_resp):
        res = Login().login(req_body)
        # assert res['msg'] == exp_resp['msg']
        ApiAssert.api_assert(res,'==',exp_resp,assert_info='msg',msg='登录断言操作')

if __name__ == '__main__':
    pytest.main([__file__,'-vs'])