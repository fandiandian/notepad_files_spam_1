# Barnsley fern








import turtle
import random
import sys

def data_of_bf(x = 0):
    if x == 0:
        probabilities = [0.01, 0.85, 0.07, 0.07]
        coefficient_x = [[0.00, 0.00, 0.500],
                         [0.85, 0.04, 0.075],
                         [0.20, -0.26, 0.400],
                         [-0.15,0.28, 0.575]]

        coefficient_y = [[0.00, 0.16, 0.00],
                         [-0.04, 0.85, 0.180],
                         [0.23, 0.22, 0.045],
                         [0.26, 0.24, -0.086]]
        return probabilities, coefficient_x, coefficient_y
    else:
        while True:
            probabilities = eval(input('请输入概率列表(1阶 1x4):'))
            coefficient_x = eval(input('请输入 x 坐标系数列表(2阶 4x3):'))
            coefficient_y = eval(input('请输入 y 坐标系数列表(2阶 4x3):'))
            try:
                total_0, total_1, total_2 = 0, 0, 0
                for i_0 in range(4):
                    total_0 += probabilities[i_0]
                for i_1 in range(4):
                    for j_1 in range(3):
                        total_1 += coefficient_x[i_1][j_1]
                for i_2 in range(4):
                    for j_2 in range(3):
                        total_2 += coefficient_x[i_2][j_2]
            except:
                again = input(' -0.0- 数据输入错误 -0.0- ... 是否重新输入? [Y/N]:')
                if again in ['Y', 'y']:
                    continue
                else:
                    print('程序退出....')
                    sys.exit()      # 直接退出程序
    # 使用管道实现数据和程序分离的方法还是有的没搞清楚。还有待研究。。。


def set_up():
    turtle.setup(1000,800)
    turtle.pu()
    turtle.pensize(-2)
    turtle.hideturtle()


def dot(x, y):
    turtle.goto(x, y)
    turtle.dot()


def discrete(lst):
    lst1 = [lst[0]]
    length = len(lst)
    for i in range(1,length):
        lst1.append(round(lst1[i-1]+lst[i],2))
    return lst1


def get_probably_num(lst):
    x = random.random()
    if x <= lst[0]:
        return 0
    elif lst[0] < x and x <= lst[1]:
        return 1
    elif lst[1] < x and x <= lst[2]:
        return 2
    else:
        return 3


def barnsley_fern(n):
    d_o_bf = data_of_bf()
    d_list = discrete(d_o_bf[0])
    x, y = 0, 0
    for i in range(n):
        r = get_probably_num(d_list)
        x = d_o_bf[1][r][0]*x + d_o_bf[1][r][1]*y + d_o_bf[1][r][2]
        y = d_o_bf[2][r][0]*x + d_o_bf[2][r][1]*y + d_o_bf[2][r][2]
        dot(x*500 - 300, y*500 - 300)
        print('\r {}'.format(i), end = '')


def main():
    print('_*'*10 + 'barnsley fern' + '*_'*8)
    n = eval(input('请输入描点的数量:'))
    set_up()
    turtle.tracer(False)
    barnsley_fern(n)
    turtle.tracer(True)
    turtle.done()

if __name__ == '__main__': main()




























