"""
__author__ = 'xumingming'
"""

import json


class RPCProxy(object):
    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        def call_rpc(*args, **kwargs):
            self._connection.send(json.dumps((name, args, kwargs)))
            result = json.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            return result
        return call_rpc


