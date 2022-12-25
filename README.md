# Описание

В своей работе столкнулся с необходимостью получить пути групп ГитЛаба в том виде, в котором их отдает GitLab API, для их последующего использования. В скрипте учтена ситуация, когда групп очень много.

# Настройка venv и скачивание зависимостей:

```
python3 -m venv .sonargroups --prompt SonarGroups
source .sonargroups/bin/activate
python3 -m pip install -r requirements.txt
```