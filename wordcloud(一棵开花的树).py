import jieba
import wordcloud

txt = '如何让你遇见我 在我最美丽的时刻 \
为这 我已在佛前求了五百年 求佛让我们结一段尘缘 佛於是把我化做一棵树 长在你必经的路旁 \
阳光下 慎重地开满了花 朵朵都是我前世的盼望 \
当你走近 请你细听 那颤抖的叶 是我等待的热情 \
而当你终於无视地走过 在你身後落了一地的 朋友啊 那不是花瓣 那是我凋零的心'

txt = ' '.join(jieba.lcut(txt))

w = wordcloud.WordCloud(width = 1000, height = 800, font_path = 'msyh.ttc', background_color = 'white')
w.generate(txt)
w.to_file('c:/Users/刘小北/Desktop/慕课截图/wordcloud/一颗开花的树.jpg')