#coding=utf8

DATABASE_ENGINE = '{}://{}@{}:{}'

DATETIME_FMT = '%Y-%m-%d %H:%M:%S'

SESSION_KEY = 'user_api:session:users'

class UserConst(object):

    # user status
    INIT = 0
    LOGGED = 2
    EXIST = 1 #存在未登录
    NULL = -1
