# Django-REST-Framework-easy-sample
Django-REST-Frameworkの簡単なサンプル。


Overview

## Description

・IoTシステムをイメージしたサンプルアプリです。

紹介記事：https://qiita.com/okoppe8/items/1c66a7f57d855f3f9b02



## Usage

Windows 

```
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
manage.py migrate
manage.py createsuperuser 
manage.py prepare_dummydata
manage.py runserver
```

Open URL http://localhost:8000
