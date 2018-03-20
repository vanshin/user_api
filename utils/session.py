#coding=utf8

'''处理session相关'''

from model.user import User

from .tools import get_uuid
from .runtime import kotori, dbsess
from .error import ParamExcp, UserExcp
from .constants import SESSION_KEY, UserConst


class LoginUser():

    def __init__(self, username='', password='', session_id=None):
        self.username = username
        self.password = password
        self.status = UserConst.INIT
        self.info = {
            'username': self.username,
        }
        self.load(session_id)

    def _handle_bytes(self, value):
        ret = ''
        if isinstance(value, dict):
            ret = {}
            for k,v in value.items():
                ret[k.decode()] = v.decode()
        elif isinstance(value, bytes):
            ret = value.decode()
        return ret

    def load(self, session_id=None):
        ret = self._handle_bytes(kotori.hgetall(session_id))
        if ret:
            self.status = UserConst.LOGGED
            self.info.update(ret)

    def __getattr__(self, item):
        if item in self.info:
            return self.info[item]
        return None

    def is_login(self):
        '''是否登录'''
        ret = False
        if self.status == UserConst.LOGGED:
            ret = True
        return ret

    def logout(self, session_id):
        '''删除session'''
        return kotori.delete(session_id)

    def check_user(self):
        '''检查用户是否存在和密码'''
        searched_user = dbsess.query(User).filter(User.username==self.username, User.password==self.password).one()
        self.status = UserConst.EXIST
        if not searched_user:
            self.status = UserConst.NULL
            return False
        self.info['userid'] = searched_user.id
        return True

    def login(self, **kwargs):
        '''登录'''

        if self.status != UserConst.EXIST:
            raise UserExcp('not exist')

        kwargs['username'] = self.username
        kwargs['password'] = self.password
        kwargs.update(self.info)

        self.session_id = get_uuid()
        kotori.hmset(self.session_id, kwargs)
        self.status = UserConst.LOGGED
        for k,v in kwargs.items():
            self.info[k] = v
        return self.session_id


