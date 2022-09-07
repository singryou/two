
from common.baseAPI import BaseAPI
from utils.handle_MD5_RSA import get_md5_data
from configs.config import NAME_PWD

class Login(BaseAPI):
    def login(self,data,get_token=False):
        data['password'] = get_md5_data(data['password'])
        resp = self.request_send(data)
        if get_token:
            return resp['data']['token']
        else:
            return resp

if __name__ == '__main__':
    resp = Login().login(NAME_PWD,get_token=False)
    print(resp)