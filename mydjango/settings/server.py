from .base import *

import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db', # DB명
        'USER': 'python', # 데이터베이스 계정
        'PASSWORD':'python', # 계정 비밀번호
      #   'HOST':'localhost', # 로컬 환경 데이터베이스 IP
        'HOST':'mysql-svc', # 서버 환경 데이터베이스 IP
        'PORT':'3306', # 데이터베이스 port
    }
}

CSRF_TRUSTED_ORIGINS=['http://*.54.254.252.127']
