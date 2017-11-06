"""
__author__ = 'xumingming'

"""
import json

from multiprocessing.connection import Listener
from threading import Thread


class RPCHandler(object):
    def __init__(self):
        self._function_list = {}

    def register_function(self, func):
        self._function_list[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                func_name, args, kwargs = json.loads(connection.recv())
                # run rpc and rend the result
                try:
                    result = self._function_list[func_name](*args, **kwargs)
                    connection.send(json.dumps(result))
                except Exception as e:
                    connection.send(json.dumps(e))
        except EOFError:
            pass


class RPCServer(object):
    def __init__(self, handler, address, authkey):
        self.handler = handler
        self.address = address
        self.authkey = authkey

    def start_server(self):
        sock = Listener(address=self.address, authkey=self.authkey)
        while True:
            client = sock.accept()
            t = Thread(target=self.handler.handle_connection, args=(client,))
            t.daemon = True
            t.start()


# remote functions

def add(x, y):
    print('add: {} + {}'.format(x, y))
    return x + y


def sub(x, y):
    print('sub : {} - {}'.format(x, y))
    return x - y

# register with a handler
handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)
if __name__ == '__main__':
    # run server
    print('start server')
    RPCServer(handler, ('localhost', 17000), authkey=b'peek').start_server()