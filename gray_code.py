# 格雷码 Gray code

'''
the definition of Gray code
一个 n 位二进制的格雷码就是一个包含 2**n 种不同情况的列表，
每一种情况的 n 位二进制数与其上一种情况的 n 位二进制数正好有一位不同
n 位二进制的格雷码生成方式如下：
    1  n 位格雷码的 前 2**(n-1) 个代码字等于 n-1 位格雷码的代码字，按顺序书写，加前缀 0
    2  n 位格雷码的 后 2**(n-1) 个代码字等于 n-1 位格雷码的代码字，按逆序书写，加前缀 1
'''

# using recursion to implement 使用递归实现,使用列表推导保存数据，输出格雷码

def gray_code(n):                                   # 递归，代码简单，速度较应用序慢
    if n == 0: return ['']
    return ['0'+i for i in gray_code(n-1)] + ['1'+i for i in gray_code(n-1)[::-1]]


# for i in gray_code(5): print(i)

# using for_loop to implement


def gray_code_for(n):                                   # 最慢最菜的写法
    list = [False for i in range(2**n)]
    list[0] = '0'
    list[1] = '1'
    lst = list[:]
    for i in range(2, n+1):
        for j in range(2**(i-1)):
            list[j] = '0'+lst[j]
            list[j+2**(i-1)] = '1'+lst[:2**(i-1)][::-1][j]
        lst = list[:]
    return list


def gray_code_for_2(n):                                 # 优化后的应用序实现，速度优势
    list = ['0', '1']
    for i in range(1,n):
        left  = ['0'+i for i in list]
        right = ['1'+i for i in list[::-1]]
        list = left + right
    return list

import time


def main(n):
    a = time.perf_counter()
    for i in gray_code(n): print(i)
    b = time.perf_counter()
    gray_code_for(n)
    c = time.perf_counter()
    gray_code_for_2(n)
    d = time.perf_counter()
    print(b-a, c-b, d-c)        # 递归时间  垃圾时间  应用序时间


if __name__ == '__main__':
    main(3)    # >>> 0.001174527398641972  0.002195796209085674  0.0001979732319710389
    # main(17)    # >>> 0.23723541986879834   46.98887458702955     0.02618878659134083