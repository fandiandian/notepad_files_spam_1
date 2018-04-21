# 科赫雪花 Koch Snowflake vision_2

print('####### 科赫雪花 Koch Snowflake #######')
import turtle as t
def k_snow(n, l) :
    if n == 0 :
        t.fd(l)
    else :
        for i in [0, 60, -120, 60] :
            t.left(i)
            k_snow(n - 1, l/3.0)

n = eval(input('你想要画出几阶的科赫雪花？\n'))
t.hideturtle()
t.speed(20)
t.pu()
t.goto(-200,200 )
t.pd()

for i in [0, 120, 120] :
    t.right(i)
    k_snow(n, 400)
t.done()