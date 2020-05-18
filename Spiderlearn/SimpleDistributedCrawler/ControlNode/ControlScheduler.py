#coding:utf-8

from py文件.Spiderlearn.SimpleDistributedCrawler.ControlNode.UrlManager import UrlManager
from py文件.Spiderlearn.SimpleDistributedCrawler.ControlNode.DataMemory import DataOutput
import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import Queue,Process
class NodeManager(BaseManager):
    def start_Manager(self,url_q,result_q):
        """
        create a distribute manager
        :param url_q: the queue of UrlManager give url to SpiderNode
        :param result_q: the queue of SpiderNode give url to UrlManager
        :return:
        """
        # 第二部：把创建的两个队列注册在网络上，利用register方法，callable参数关联Queue对象，
        # 将Queue对象在网络中暴露
        BaseManager.register('get_task_queue',callable=lambda:url_q)
        BaseManager.register('get_result_queue',callable=lambda:result_q)
        # 第三部：绑定端口 8001，设置验证口令'baike',这个相当于对象的初始化
        manager = BaseManager(address=('127.0.0.1', 8010), authkey=b'baike')
        return manager

    def url_manager_proc(self,url_q,conn_q,root_url):
        """
        from conn_q get new url to UrlManager and after
        Duplicate removal(qu_chong),get url to url_queue
        to give SpiderNode
        :param url_q:the queue of UrlManager give url to SpiderNode
        :param conn_q:the queue of DataGetProgress get new url to UrlManager
        :param root_url:
        :return:
        """
        url_manager = UrlManager()
        url_manager.add_new_url(root_url)
        while True:
            while (url_manager.has_new_url()):

                new_url = url_manager.get_new_url()
                #give url to work-node
                url_q.put(new_url)
                print('old_url=',url_manager.old_url_size())

                # when get 2000,close
                if (url_manager.old_url_size() > 200):
                    # tell work-node end work
                    url_q.put('end')
                    print('Control Node tell end')
                    # end UrlManager and save set
                    url_manager.save_progress('new_urls.txt', url_manager.new_urls)
                    url_manager.save_progress('old_urls.txt', url_manager.old_urls)
            #give url from result_solve_proc to UrlManager
            try:
                if not conn_q.empty():
                    urls = conn_q.get()
                    url_manager.add_new_urls(urls)
            except BaseException as e:
                time.sleep(0.1)

    def result_solve_proc(self,result_q,conn_q,store_q):
        """
        from result_queue get datas,and give data.url to conn_q then give UrlManager
        give data.title and data.summary to store_q then give DataMemoryProc
        :param result_q:  the queue of SpiderNode give url to UrlManager
        :param store_q: the queue of DataGetManager give datas to DataMemoryProc
        :return:
        """
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    # print(content)
                    if content['new_urls'] == 'end':
                        print('Result_sove_proc get news and end')
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])
                    store_q.put(content['data'])
                else:
                    time.sleep(0.1)
            except BaseException as e:
                time.sleep(0.1)

    def store_proc(self,store_q):
        """
        get datas from store_q and then datamemory
        :param store_q:
        :return:
        """
        output = DataOutput()
        #print(store_q)
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data == 'end':
                    print('Store_proc get news end')
                    output.output_end(output.filepath)
                    return
                output.store_data(data)
            else:
                time.sleep(0.1)

if __name__ == '__main__':
    url_q = Queue()
    result_q = Queue()
    store_q = Queue()
    conn_q = Queue()

    node = NodeManager()
    manager = node.start_Manager(url_q,result_q)
    url_manager_proc = Process(target=node.url_manager_proc,args=(url_q,
        conn_q,'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB',))
    result_solve_proc = Process(target=node.result_solve_proc,args=(result_q,
        conn_q,store_q))
    store_proc = Process(target=node.store_proc,args=(store_q,))

    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    # server = manager.get_server()
    # server.serve_forever()
    manager.get_server().serve_forever()