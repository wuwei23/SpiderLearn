import re
import json

class HtmlParser(object):

    # 从选购电影页面中解析出所有电影信息，组成一个list
    def parser_url(self, page_url, response):
        pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls = pattern.findall(response)
        if urls != None:
            # 将urls去重
            return list(set(urls))
        else:
            return None

    # 解析正在上映的电影
    def __parser_release(self, page_url, value):
        '''
            解析已经上映的电影
            :param page_url：电影链接
            :param value: json数据
            :return
        '''
        try:
            isRelease = 1
            movieRating = value.get('value').get('movieRating')
            movieTitle = value.get('value').get('movieTitle')
            try:
                boxOffice = value.get('value').get('boxOffice')
                TotalBoxOffice = boxOffice.get("TotalBoxOffice")
                TotalBoxOfficeUnit = boxOffice.get("TotalBoxOfficeUnit")
                TodayBoxOffice = boxOffice.get("TodayBoxOffice")
                TodayBoxOfficeUnit = boxOffice.get("TodayBoxOfficeUnit")
                ShowDays = boxOffice.get('ShowDays')
            except Exception as e:
                boxOffice = '0'
                TotalBoxOffice = '0'
                TotalBoxOfficeUnit = '元'
                TodayBoxOffice = '0'
                TodayBoxOfficeUnit = '元'
                ShowDays = 'none'


            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')

            MovieId = movieRating.get("MovieId")
            UserCount = movieRating.get("Usercount")
            AttitudeCount = movieRating.get("AttitudeCount")

            try:
                Rank = boxOffice.get('Rank')
            except Exception as e:
                Rank = 0
            # 返回所提取的内容
            return (
            MovieId, movieTitle, RatingFinal, ROtherFinal, RPictureFinal, RDirectorFinal, RStoryFinal, UserCount,
            AttitudeCount, TotalBoxOffice + TotalBoxOfficeUnit, TodayBoxOffice + TodayBoxOfficeUnit, Rank, ShowDays,
            isRelease)
        except Exception as e:
            print(e, page_url, value)
            return None

    # 解析未上映的电影
    def __parser_no_release(self, page_url, value, isRelease=0):
        '''
            解析未上映的电影信息
            :param page_url
            :param value
            : return
        '''
        try:
            movieRating = value.get('value').get('movieRating')
            movieTitle = value.get('value').get('movieTitle')

            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')

            MovieId = movieRating.get("MovieId")
            UserCount = movieRating.get("Usercount")
            AttitudeCount = movieRating.get("AttitudeCount")

            try:
                Rank = value.get('value').get('hotValue').get('Ranking')
            except Exception as e:
                Rank = 0
            # 返回所提取的内容
            return (
            MovieId, movieTitle, RatingFinal, ROtherFinal, RPictureFinal, RDirectorFinal, RStoryFinal, UserCount,
            AttitudeCount, u'无', u'无', Rank, 0, isRelease)
        except Exception as e:
            print(e, page_url, value)
            return None

    # 解析电影中的json信息
    def parser_json(self, page_url, response):
        """
            解析响应
            :param response
            :return
        """
        # 将"="和";"之间的内容提取出来
        pattern = re.compile(r'=(.*?);')
        result = pattern.findall(response)[0]
        if result != None:
            # json模块加载字符串
            value = json.loads(result)
            # print(result)
            try:
                isRelease = value.get('value').get('isRelease')
            except Exception as e:
                print(e)
                return None
            if isRelease:
                '''
                    isRelease:0 很长时间都不会上映的电影；1 已经上映的电影； 2 即将上映的电影
                '''
                if value.get('value').get('hotValue') == None:
                    # 解析正在上映的电影
                    #print(self.__parser_release(page_url, value))
                    return self.__parser_release(page_url, value)
                else:
                    # 解析即将上映的电影
                    #print(self.__parser_no_release(page_url, value))
                    return self.__parser_no_release(page_url, value)
            else:
                # 解析还有很长时间才能上映的电影
                #print(self.__parser_no_release(page_url, value))
                return self.__parser_no_release(page_url, value)
