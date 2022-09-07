import traceback
import inspect
import os

import requests
from utils.handle_path import configs_path
from utils.handle_yaml import get_yaml_data
from utils.handle_loguru import log
from configs.config import HOST

class BaseAPI:
    def __init__(self,token=None):
        if token:
            self.header = {'Authorization':token}
        else:
            self.header = None

        self.data = get_yaml_data(os.path.join(configs_path,'apiPathConfig.yaml'))[self.__class__.__name__]

    def request_send(self,params=None,data=None,json=None,files=None,id=''):
        try:
            api_data = self.data[inspect.stack()[1][3]]
            resp = requests.request(
                url = f'{HOST}{api_data["path"]}',
                method = api_data['method'],
                params=params,
                data=data,
                json=json,
                files=files,
                headers=self.header
            )
            log.info(f'模块名:{self.__class__.__name__}')
            log.info(f'请求url:{resp.request.url}')
            log.info(f'请求方法:{resp.request.method}')
            log.info(f'请求体:{resp.request.body}')
            log.info(f'响应体:{resp.json()}')
            return resp.json()
        except Exception as error:
            log.error(traceback.format_exc())
            raise error

    def query(self,data):
        return self.request_send(params=data)

    def add(self,data):
        return self.request_send(data=data)

    def update(self,data):
        return self.request_send(data=data)

    def delete(self,id):
        return self.request_send(id=id)

    def file_upload(self,file_path:str):
        file_name = file_path.split('/')[-1]
        file_type = file_name.split('.')[-1]
        file = {'file:'(file_name,open(file_path,'rb'),file_type)}
        return self.request_send(files=file)


    """
    Content-Disposition: form-data; name="file";    filename="QQ截图20200724100920.png"
Content-Type: image/png

    文件上传格式： 文件路径、文件名、文件类型
    路径: xx/123.png
    {‘file’:(文件名，文件对象本身，文件类型)}---转化
    {‘file’:('123.png'，open('xx/123.png','rb')，'png')}
    """