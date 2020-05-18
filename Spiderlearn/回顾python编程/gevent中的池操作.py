#对gevent协程使用流程进行改写
from gevent import monkey
monkey.patch_all()
import urllib.request
from gevent.pool import Pool

def run_task(url):
    print('Visit ---> %s' % url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        print('%d bytes received from %s.' % (len(data), url))
    except Exception as e:
        print(e)
    return 'url:%s ---> finish' % url
if __name__ == '__main__':
    pool = Pool(2)
    urls = ['http://github.com/','http://www.python.org/','http://www.cnblogs.com/']
    results = pool.map(run_task,urls)#分配协程任务
    print(results)

#使用pool进行管理，先访问前两个网址，再访问最后一个