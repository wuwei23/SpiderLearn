#coding:utf-8
import pickle
import hashlib

class UrlManager(object):
    def __init__(self):
        self.new_urls = self.load_progress('new_urls.txt')#not crawle urls set
        self.old_urls = self.load_progress('old_urls.txt')#crawle urls set

    def has_new_url(self):
        """
        judge  is have not-crawle url
        :return:
        """
        return self.new_url_size() !=0

    def get_new_url(self):
        """
        get a new  not-crawle url
        :return:
        """
        new_url = self.new_urls.pop()
        #Crawled URL performs MD5 character processing to reduce memory consumption.
        #create md5 object
        m = hashlib.md5()
        #Generating an encrypted string
        m.update(new_url.encode("utf-8"))
        #m.hexdigest():Getting the encrypted string加密
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url

    def add_new_url(self,url):
        """
        put new url on not-crawle urls
        :param url: one url
        :return:
        """
        if url is None:
            return
        m = hashlib.md5()
        m.update(url.encode("utf-8"))
        url_md5 = m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        """
        put new url on not-crawle urls
        :param url: urls
        :return:
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        """
        get size of not-crawle url set
        :return:
        """
        return len(self.new_urls)

    def old_url_size(self):
        """
        get size of crawled url set
        :return:
        """
        return len(self.old_urls)

    def save_progress(self,path,data):
        """
        save progress
        :param path:file path
        :param data:data
        :return:
        """
        with open(path,'wb') as f:
            pickle.dump(data,f)

    def load_progress(self,path):
        """
        load progress from file
        :param path: file path
        :return: set
        """
        print('[+] from file load progress %s' % path)
        try:
            with open(path,'rb') as f:
                tmp = pickle.load(f)
                return tmp
        except:
            print('[!] not progress file,create: %s' % path)

            return set()