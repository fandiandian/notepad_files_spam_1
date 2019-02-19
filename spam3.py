# 定向爬取 最好大学网 上的中国大学排名
# 技术路线 使用 Requests-bs4

'''
程序结构：
    1、get_html_info() 使用requests库，通过 URL 获取网页信息
    2、universities_ranking() 提取关键信息，并保存到合适的文件结构中
    3、print_ranking() 结果的输出
        --> 可以将得到的数据输出到 cvs 文件中
'''

# 使用requests前,对url对于应的那个网页需要进行内容查看（F12）
    # 所需的要的信息是否在HTML的文件中（静态文件）
# 查看网站的 robots.txt 协议，做合规分析

import requests, re, sys, bs4
from bs4 import BeautifulSoup

def get_html_info(url):
    try:
        r = requests.get(url)
        r.raise_for_status() # 如果网页状态码不是 200，则发起异常（重要）
        r.encoding = r.apparent_encoding # 网页内容重现编码
        return r.text
    except:
        print('出现异常，未能成功获取网页 ~0.0~ ')
        # sys.exit()会引发一个异常：SystemExit，如果这个异常没有被捕获，那么python解释器将会退出。
        # 如果有捕获此异常的代码，那么程序余下代码还是会执行。
        # 推荐使用 sys.exit() 来退出程序（这样比较优雅，不会在console出现异常信息）
        sys.exit() 

def universities_ranking(html):
    # 构建二维数组来保存获取到的数据
    u_data = [] # 二维数组
    u_in_data = [] # 二维数组中的一维数组
    # 将 html 文件转化成 BeautifulSoup 类型
    soup = BeautifulSoup(html, 'html.parser')
    # 获取表头信息
    for titles in soup.tr('th'):
        if len(titles.text) < 5:
            u_in_data.append(titles.text)
        else:
            u_in_data += titles.text.split('\n')[1:-2]
    u_data.append(u_in_data)
    # 获取 tobody 标签下所有的 tr 子标签，单独的一个 tr 标签又包含多个 string 信息，所以需要通过双层循环获取信息
    for tr in soup.tbody('tr'):
        u_in_data = []
        for data_string in tr:
            u_in_data.append(data_string.string)
        u_data.append(u_in_data)

    return u_data

'''
关于 seek(offset[, whence]) 函数：
官方文档介绍如下：
    Change the stream position to the given byte offset. offset is interpreted relative to the position indicated by whence. The default value for whence is SEEK_SET. Values for whence are:

    SEEK_SET or 0 – start of the stream (the default); offset should be zero or positive
    SEEK_CUR or 1 – current stream position; offset may be negative
    SEEK_END or 2 – end of the stream; offset is usually negative
    Return the new absolute position.

    New in version 3.1: The SEEK_* constants.

    New in version 3.3: Some operating systems could support additional values, like os.SEEK_HOLE or os.SEEK_DATA. 
    ###*** The valid values for a file could depend on it being open in text or binary mode. ***###
    
    更改指针位置，有两个参数：
        offset : 移动的位置的大小，正数向后移动，负数向前移动
        whence : 设定指针移动的参考位置
            0 : 文件的开头位置        eg: f.seek(2, 0) 指针从文件的开始位置向后移动两个位置    offset 只能为正数
            1 : 指针当前所在位置      eg: f.seek(-2, 1) 指针从指针当前的位置向前移动两个位置   offset 可正可负
            2 : 文件的结束位置        eg: f.seek(-2, 2) 指针从文件的结束位置向前移动两个位置   offset 一般为负数
            
    指针移动函数有一个约束条件:
        1 当文件以二进制的形式打开时，所有的指针移动方式均可以得到执行
        2 当文件以文本文档形式打开时，指针的移动只有从文件的开头位置往后移动
        
    但是以二进制的形式打开文件，生成的文件，会出现编码的问题，Excel 会以 unicode 的编码方式打开，导致出现乱码
'''

def output_to_csv(data):
    f = open('f:/web_crawler/universities_ranking.csv','w')
    for _i in data:
        for _j in _i[:-1]:
            f.write(str(_j)+ ',')
        f.write(_i[-1] + '\n')
    f.close

def output_to_csv_binary(path, data):
    f = open(path, 'wb')
    for _i in data:
        for _j in _i:
            if _j == None:
                _j = '/'
            f.write(_j.encode('utf-8') + ','.encode('utf-8'))
        f.seek(-1, 1) # 使用 seek() 改变指针位置
        f.write('\n'.encode('utf-8'))
    f.close()
    # 这里遇到了一个问题，以二进制的方式创建的文件，保存后，用 excel 打开后为乱码，应该是编码的问题
    # 目前还没有发现怎么在 python 中解决这个问题
    # 目前的解决办法是：使用文本文档的方式打开 --> 另存为 --> 选择编码方式为: utf-8  --> 保存，在删除原文件（用户体验极差）

# 通过读取文件的方式获取以保存的数据，格式化输出
'''
中文字符的对齐问题
因为中文字符所占的宽度比英文字符大，所以在对齐的问题上，会出现错乱对不齐的情况
解决办法之一：将填充的西文空格用中文空格代替
    chr(12288) --> 对应的就是中文空格
    在 format() 中可以通过占位的方式将填充个西文空格换成中文空格
        eg： print('{0:{1}^10}'.format('湖南永州', chr(12288)))
'''
def print_ranking(path):
    with open(path, 'rt', encoding = 'utf-8') as f:
        title = f.readline().split(',')
        print('{0:^4}*{1:{3}^12}* {2:<20}'.format(title[0], title[1], title[3], chr(12288))) # 缩减中文字符的占位长度以美化输出
        for lines in f.readlines():
            lines = lines.split(',')
            print('{0:^6}*{1:{3}^12}* {2:<20}'.format(lines[0], lines[1], lines[3], chr(12288)))

def main():
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    path = 'f:/web_crawler/universities_ranking_binary.csv'
    g_h_info = get_html_info(url)
    u_ranking = universities_ranking(g_h_info)
    output_to_csv(u_ranking)
    output_to_csv_binary(path, u_ranking)
    print_ranking(path)

# 调用函数
main()




































































































