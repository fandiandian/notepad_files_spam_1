import jieba
import wordcloud
from scipy.misc import imread

mask = imread('c:/Users/刘小北/Desktop/慕课截图/wordcloud/map_of_china.jpg')

with open('f:/notepad_files_spam/auxiliary_files/新时代特色社会主义.txt', 'rt') as f :
    txt = f.read()
w = wordcloud.WordCloud(width = 1000, height = 800, font_path = 'msyh.ttc', background_color = 'white', max_words = 300, mask = mask)
w.generate(' '.join(jieba.lcut(txt)))
w.to_file('c:/Users/刘小北/Desktop/慕课截图/wordcloud/新时代特色社会主义2.jpg')