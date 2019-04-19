
from base.handler import BaseView


class User(BaseView):

    async def get(self):

        self.args_idft = {
            'str': ['username', 'mobile', 'email'],
            'int': ['type']
        }

        v = self.build_args()

        pass

    async def post(self):
        pass
