import yaml
def get_yaml_data(file_path:str):
    with open(file_path,encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())

def get_yaml_case(file_path:str):
    list_data = []
    res = get_yaml_data(file_path)
    for i in res:
        list_data.append(i['detail'],i['data'],i['resp'])
    return list_data

if __name__ == '__main__':
    res = get_yaml_data('../configs/apiPathConfig.yaml')
    print(res)