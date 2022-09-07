
import requests
from utils.handle_MD5_RSA import get_md5_data
from utils.handle_MD5_RSA import RsaEndecrypt
from configs.config import NAME_PWD

def login(indata):
    url = 'http://121.41.14.39:8082/account/loginRsa'
    # 1、使用MD5方式将密码加密
    get_md5_text = get_md5_data(indata['password'])
    # 2、使用RSA方式将MD5加密后的密文进行加密
    get_rsa_text = RsaEndecrypt().encrypt(get_md5_text)
    # 3、将加密后的密码重新赋值给形参密码
    indata['password'] = get_rsa_text
    # 4、签名操作：将用户名和RSA加密后的密码再进行整体MD5加密
    sign = get_md5_data(indata['username'] + get_rsa_text)
    # 5、将签名重新赋值给形参签名
    indata['sign'] = sign

    payload = indata

    res = requests.post(url,data=payload)
    print(res.text)

if __name__ == '__main__':
    login(NAME_PWD)