class Url(object):
    def __init__(self, url):
        self.url = url

    def __getattribute__(self, item):
        print 'get attribute'
        print item
        return super(Url, self).__getattribute__(item)

    # def __getattr__(self, item):
    #     print 'get attr'
    #     print item
    #     return 'sssss'

url = Url('www.baidu')
# url.url
url.get