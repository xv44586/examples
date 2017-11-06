"""
__author__ = 'xumingming'
"""

from multiprocessing.connection import Client
from prcProxy import RPCProxy

if __name__ == '__main__':
    client = Client(('localhost', 17000), authkey=b'peek')
    proxy = RPCProxy(client)
    print(proxy.add(1, 2))