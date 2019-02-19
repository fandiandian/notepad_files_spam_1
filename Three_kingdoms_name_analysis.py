# 三国演义的人物名字的出场次数分析
# three kingdomes person's name analysis
# 使用 jieba 库进行中文分词处理三国演义的文本文档

'''
利用字典表进行数据统计，最后将字典表的数据提取，列表化后，排序输出结果
'''

import jieba
from collections import defaultdict
# 打开文件
f = open('f:/notepad_files_spam/auxiliary_files/threekingdoms.txt', 'rt', encoding = 'utf-8')
# 读取文件，并将文件进行分词处理
t_txt = jieba.lcut(f.read())
# 初始化数据字典表
def letter_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        if len(letter) > 1:
            frequencies[letter] += 1
    return frequencies

# 获取字典表中的数据，并列表化
t_dict = letter_frequency(t_txt)
t_list = list(t_dict.items())
# 对列表进行排序
t_list.sort(key = lambda x: x[1], reverse = True)

for i in range(10) :
    print('{} 出现的次数为: {:>4}'.format(t_list[i][0], t_list[i][1]))

# 运行结果
# 曹操 出现的次数为:  953
# 孔明 出现的次数为:  836
# 将军 出现的次数为:  772
# 却说 出现的次数为:  656
# 玄德 出现的次数为:  585
# 关公 出现的次数为:  510
# 丞相 出现的次数为:  491
# 二人 出现的次数为:  469
# 不可 出现的次数为:  440
# 荆州 出现的次数为:  425