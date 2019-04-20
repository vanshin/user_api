
from altools.base.handler import BaseView
from altools.model.user import User
from altools.base.output import output


class UserInfo(BaseView):

    async def post(self):

        self.args_idft = {
            'int': ['type', 'status'],
            'str': [
                'username', 'mobile', 'email',
                'password'
            ],
        }

        v = await self.build_args()

        # 登陆地址
        v['login_ip'] = self.remote_addr

        await User.add_user(**v)

        return output()

    async def get(self):
        pass
