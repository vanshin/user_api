#coding=utf8

'''用户相关接口'''

import os
import datetime

from flask import request, current_app

from .base import build_args
from . import main

from utils.constants import DATETIME_FMT
from utils.output import output
from utils.session import LoginUser
from utils.error import UserExcp
from model.user import User

@main.route('/user', methods=['POST'])
def post_user():
    '''添加一个用户'''
    now = datetime.datetime.now()

    #
    args_list = [
        ('password', 'str', 'must'),
        ('username', 'str', 'must'),
        ('email', 'str', 'must'),
        ('mobile', 'str', 'must'),
        ('status', 'int', 'default', 1),
        ('type', 'int', 'default', 1),
        ('regi_time', 'datetime', 'default', now.strftime(DATETIME_FMT)),
        ('login_address', 'str', 'default', request.remote_addr),
    ]
    args = build_args(request.values, args_list)
    user = User(**args)
    current_app.dbsess.add(user)
    current_app.dbsess.commit()

    return output()

@main.route('/login', methods=['POST'])
def post_login():
    '''登录'''

    args_list = [
        ('username', 'str', 'must'),
        ('password', 'str', 'must'),
    ]
    ret = {}
    args = build_args(request.values, args_list)
    login_user = LoginUser(args['username'], args['password'])
    if login_user.check_user():
        session_id = login_user.login()
        ret['session_id'] = session_id
    else:
        raise UserExcp('用户可能不存在或者账号密码不对')
    return output(data=ret)

