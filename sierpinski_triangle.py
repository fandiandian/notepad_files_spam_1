# sierpinski triangle  谢尔宾斯基三角

'''
概述
1 给定等边三角形的一个顶点绘制一个点
2 然后在三个顶点中随机选择一个顶点，并在前一个绘制点和随机选择的顶点之间连线的中点位置绘制一个点
3 重复上述步骤，每次循环过程，均随机从三角形的顶点中选取一个，并与前一个连线的中点构成新的连线，并在新的连线的中点绘制一个点

使用 turtle 模块绘制，以后有时间使用 pygame 库来绘制
'''

import turtle
import random


def random_point():
    return random.randint(0,2)


def sierpinski_triangle(n, triangle):
    x0, y0 = triangle[random_point()]
    dot(x0, y0)
    for i in range(n):
        x1, y1 = triangle[random_point()]
        x0, y0 = midpoint(x0, y0, x1, y1) # 更新中点坐标
        dot(x0, y0)
        print('\r{}'.format(i), end = '')

def _set_sreen(length):
    turtle.setup(1000, 800)
    turtle.pu()
    turtle.hideturtle()
    turtle.pensize(-2)

def dot(x, y):
    turtle.goto(x,y)
    turtle.dot()

def midpoint(x0, y0, x1, y1):
    return (x0+x1)/2, (y0+y1)/2

def main():
    length = eval(input('请输入等边三角形的边长:'))
    times = eval(input('请输入绘制的次数:'))
    triangle = [(-length/2, -1.732051*length/4), (length/2, -1.732051*length/4), (0, 1.732051*length/4)]
    _set_sreen(length)
    turtle.tracer(False)   # 加快绘制过程，在背景画布上绘制
    sierpinski_triangle(times, triangle)
    turtle.tracer(True)    # 背景画布显示（一次性全部显示，没有绘制过程）
    turtle.done()


if __name__ == '__main__': main()






































