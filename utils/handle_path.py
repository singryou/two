import os

# 工程路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# configs路径
configs_path = os.path.join(project_path,'configs')

# data路径
data_path = os.path.join(project_path,'data')

# report路径
report_path = os.path.join(project_path,r'outfiles/report/tmp')

# logs路径
log_path = os.path.join(project_path,r'outfiles/logs')