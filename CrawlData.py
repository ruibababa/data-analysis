# @Author  : ShiRui
import requests
import time
import xlwt


class PythonWorkAnalysis:

    @staticmethod
    def create_table():  # 定义一个函数，用来创建Excle表格

        title = [
            '职位', '经验', '学历', '地点', '工资', '公司', '福利'
        ]   # 每列的列名

        wbk = xlwt.Workbook()  # 创建一个工作区
        sheet = wbk.add_sheet('datas')  # 页脚
        for i in range(len(title)):
            sheet.write(0, i, title[i])  # 创建表头

        return sheet, wbk

    @staticmethod
    def collecting_data():

        datas = []  # 设置一个列表，存放数据
        url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"  # 访问的网站
        header = {
            'Host': 'www.lagou.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.lagou.com/jobs/list_Java?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Anit-Forge-Token': 'None',
            'X-Anit-Forge-Code': '0',
            'Content-Length': '24',
            'Cookie': 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1526999483,1527172516,1527509897,1527509901; _ga=GA1.2.1119628386.1522855105; user_trace_token=20180404231902-8182e3f5-381b-11e8-b413-525400f775ce; LGUID=20180404231902-8182e714-381b-11e8-b413-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; WEBTJ-ID=20180528201816-163a6af4d221f9-08a294f453ba4f-46514133-1049088-163a6af4d23123; LGSID=20180528201913-5552632f-6271-11e8-adad-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DuHLK65HE50JshAG6GtlWwY16UdLnvezTfaaTEMtBX2PvTV1HsliPzAGQdRxuUiEE%26wd%3D%26eqid%3Ded4adeb900000fca000000065b0bf3b8; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F; LGRID=20180528203532-9c6e6941-6273-11e8-adae-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1527510879; _gid=GA1.2.145013823.1527509897; JSESSIONID=ABAAABAACEBACDGE429A300E6A8DC217E51550B216A36D9; SEARCH_ID=663116997067435388edb230276acce7; TG-TRACK-CODE=search_code; _gat=1',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'

        }  # 响应头，反扒需要

        for i in range(1, 15):

            form = {
                'first': 'false',
                'kd': '数学教师',
                'pn': i
            }  # 因为这个网站是post请求，所以提交的使用form提交。 pn表示的是第多少页

            time.sleep(1)  # 设置请求延迟
            html = requests.post(url, data=form, headers=header)  # 返回需要的数据

            for m in range(len(html.json()['content']['positionResult']['result'])):  # 遍历每个数据
                position = html.json()['content']['positionResult']['result'][m]['positionName']
                wordyear = html.json()['content']['positionResult']['result'][m]['workYear']
                enducation = html.json()['content']['positionResult']['result'][m]['education']
                city = html.json()['content']['positionResult']['result'][m]['city']
                salary = html.json()['content']['positionResult']['result'][m]['salary']
                companyshortname = html.json()['content']['positionResult']['result'][m]['companyShortName']
                positionAdvantage = html.json()['content']['positionResult']['result'][m]['positionAdvantage']

                content = [position, wordyear, enducation, city, salary, companyshortname, positionAdvantage]  # 存入content列表
                datas.append(content)  # datas存入

        sheet, wbk = PythonWorkAnalysis.create_table()  # 接收返回的sheet，和表格wbk

        for i in range(len(datas)):  # 遍历datas里面的每个内容

            if i != 0:
                for j in range(7):  # 一共七个数据，所以是range（7）
                    sheet.write(i, j, datas[i][j])  # 写入

        wbk.save('PythonWorkAnalysis.xls')  # 存储下来


if __name__ == "__main__":

    PythonWorkAnalysis.collecting_data()
