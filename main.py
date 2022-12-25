import requests
import gitlab
import urllib3
import os

urllib3.disable_warnings()

### URL-s and credentials
gitlab_url = "http://gitlab.rshbdev.ru"
private_token = os.getenv('GL_TOKEN') ### Временный ApiToken GitLab

### Авторизация
s = requests.Session()
s.verify = False
gl = gitlab.Gitlab(url=gitlab_url, private_token=private_token, api_version=4, session=s)
gl.auth()

### Получаем группы из ГитЛаба.
def get_groups():
    return [i.full_path for i in gl.groups.list(as_list=False)]

if __name__ == '__main__':
    groups_path = get_groups()