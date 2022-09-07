
import traceback
from utils.handle_loguru import log

class ApiAssert:
    @classmethod
    def api_assert(cls,result,contition,exp_result,assert_info,msg='断言操作'):
        '''
        断言操作:
        :param result:响应结果
        :param contition:断言类型
        :param exp_result:预期结果
        :param assert_info:断言内容
        :param msg:注释
        :return:
        '''
        pass_msg = '断言操作，响应结果：{0}，预期结果：{1}'
        try:
            assert_type = {
                '==' : result[assert_info] == exp_result[assert_info],
                '!=' : result[assert_info] != exp_result[assert_info],
                '>' : result[assert_info] > exp_result[assert_info] if not isinstance(exp_result[assert_info],list) else False,
                '<' : result[assert_info] < exp_result[assert_info] if not isinstance(exp_result[assert_info],list) else False,
                'in' : result[assert_info] in exp_result[assert_info] if isinstance(exp_result[assert_info],list) else False,
                'not in' : result[assert_info] not in exp_result[assert_info] if isinstance(exp_result[assert_info],list) else False
            }
            if contition in assert_type:
                assert assert_type[contition]
            else:
                raise AssertionError['请输入正确的断言类型']
            log.info(f'{msg},断言类型:{contition},断言结果:{pass_msg.format(result[assert_info],exp_result[assert_info])}')
        except Exception as error:
            log.error(traceback.format_exc())
            raise error