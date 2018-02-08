#coding=utf8

'''error code'''

from . import main
from utils.output import output
from utils.error import ParamExcp

@main.errorhandler(ParamExcp)
def param_excp(e):
    return output(e.code, e.message)
