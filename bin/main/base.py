#coding-utf8

'''base'''

import os
import logging
log = logging.getLogger()

from .error import ParamExcp
from utils import valid

def build_args(value, args):
    '''build args'''
    ret = {}
    for i in args:
        log.debug('参数={}'.format(i[0]))
        if 'must' in i:
            item_value = value.get(i[0])
            if not item_value:
                raise ParamExcp('参数未填写')
            if not getattr(valid, 'is_valid_{}'.format(i[1]))(item_value):
                raise ParamExcp('不是{}类型'.format(i[1]))
            ret[i[0]] = item_value
        if 'default' in i:
            default = i[3]
            item_value = value.get(i[0], default)
            if not getattr(valid, 'is_valid_{}'.format(i[1]))(item_value):
                raise ParamExcp('不是{}类型'.format(i[1]))
            ret[i[0]] = item_value

    return ret

