
import hashlib
def get_md5_data(pwd:str,salt=''):
    # 1、创建MD5实例对象
    md5 = hashlib.md5()
    # 2、拼接盐值
    pwd += salt
    # 3、调用加密函数
    md5.update(pwd.encode('utf-8'))
    # 4、返回加密后的密文---16进制的字符串
    return md5.hexdigest()

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as pk_cipher
import base64

class RsaEndecrypt:

    def __init__(self,file_path='./'):
        # 1、公钥的文件路径
        self.file_path = file_path

    def encrypt(self,crypt_data):
        # 2、以rb模式打开公钥文件
        with open(self.file_path + 'public.pem','rb') as fo:
            # 3、读取公钥文件内容
            key_content = fo.read()
            # 4、把需要加密的数据转化为bytes
            crypt_data = crypt_data.encode('utf-8')
            # 5、将公钥文件的内容变成公钥对象
            public_key = RSA.importKey(key_content)
            # 6、使用这个公钥对象生成一个加密对象
            cipher = pk_cipher.new(public_key)
            # 7、使用加密对象加密需要加密的数据
            encrypt_data = cipher.encrypt(crypt_data)
            # 8、使用base64编码，再解码成str
            return base64.b64encode(encrypt_data).decode()

if __name__ == '__main__':
    res = RsaEndecrypt().encrypt('123456')
    print(res)