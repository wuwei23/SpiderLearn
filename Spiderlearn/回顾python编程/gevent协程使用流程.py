import gevent
from gevent import monkey
monkey.patch_all()
#把标准库中的thread/socket等给替换掉.这样我们在后面使用socket的时候可以跟
# 平常一样使用,无需修改任何代码,但是它变成非阻塞的了.
import urllib.request       #py3中的urllib2被替换成了urllib.request
def run_task(url):
    print('Visit --> %s' % url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        print('%s bytes received from %s.' % (len(data),url))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    urls = ['http://github.com/','http://www.python.org/','http://www.cnblogs.com/']
    greenlets = []
    for url in urls:
        greenlets.append(gevent.spawn(run_task,url))#spawn形成协程
    gevent.joinall(greenlets)#joinall添加这些协程任务

#三个网络操作（协程）是并发执行的，结束顺序不同，但只有一个线程
