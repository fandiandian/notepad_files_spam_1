# 练习文件

# import turtle as t

# t.setup(500,500)
# t.colormode(255)
# t.color(0, 255, 255)
# t.begin_fill()
# t.fd(50)
# t.right(90)
# t.fd(50)
# t.right(90)
# t.fd(50)
# t.right(90)
# t.fd(50)
# t.right(90)
# t.end_fill()
# t.done()

################################################

# 递归函数  阶乘
# 使用 for 循环实现
# def factorial_for_loop(n):
    # total_for = 1
    # for i in range(1, n+1):
        # total_for *= i
    # return total_for

# # print(factorical_for_loop(5))

# # 使用递归实现
# def factorial_recursion(n):
    # if n <= 1: return 1
    # return n * factorial_recursion(n-1)


    
# print(factorial_recursion(-35))  # 会产生 RecursionError: maximum recursion depth exceeded in comparison


################################################

# # 最大公约数 (greatest common divisor, gcd)
# # 可以被这两个整数整除的最大整数
# '''
# 对于正整数 p 和 q，欧几里得法的计算方式：
# 如果 p > q，则 p 和 q 的最大公约数等于 q 和 p % q 的最大公约数，以此递归类推， p % q == 0 时，q 即为两者的最大公约数
# '''

# import sys

# def euclid_gcd(p, q):
    # if q == 0: return p
    # return euclid_gcd(q, p%q)


# def main():
    # p = int(sys.argv[1])
    # q = int(sys.argv[2])
    # if q > p:
        # print('正整数 {} 和 {} 之间的最大公约数是: {}'.format(p, q, euclid_gcd(q, p)))
    # else:
        # print('正整数 {} 和 {} 之间的最大公约数是: {}'.format(p, q, euclid_gcd(p, q)))

# if __name__ == '__main__': main()

################################################

# 汉诺塔 tower of hanoi

'''
有 3 个柱子和 n 个圆盘（圆盘大小各不同），圆盘套在柱子上，小的圆盘只能套在大的圆盘之上
最初圆盘是按大小顺序套在最左边的一个柱子上，现通过中间的柱子，转移到最右边的柱子上
规则
    1 一次只能移动一个盘子
    2 不能把大的盘子放到小的盘子上
'''

# 通过递归可以很好的解决这个问题，现假设有 A B C 三根柱子，所有的圆盘位于 A 柱上，按规则经过 B 柱移动到 C 柱上

# def hanoi_tower(n, A, B, C):
    # global count

    # if n == 0: return 

    # # 将 A 柱上的 n-1 块(共 n-1 块) 利用 C 柱 移动到 B 柱
    # hanoi_tower(n-1, A, C, B)

    # # 将 A 柱上的第 n 块(共 1 块) 直接移动到 C 柱
    # # hanoi_tower(1, A, B, C)
    # count += 1    # 移动次数加一
    # print('将 {} 柱上的第 {} 块圆盘移动到 {} 柱上'.format(A, n, C))

    # # 将 B 柱上的 n-1 块(共 n-1 块) 利用 A 柱 移动到 C 柱
    # hanoi_tower(n-1, B, A, C)

# def main():
    # global count
    # count = 0
    # hanoi_tower(3, 'A', 'B', 'C')
    # print(count)


# if __name__ == '__main__': main()



# # 书上的程序：采用的带回绕的移动的方式，没有固定要移动到 C 柱，只要移动到另外一个柱上即可 
# # 其实是一样的
# def hanoi_tower_1(n, left):
    # if n == 0:  return
    # hanoi_tower_1(n-1, not left)
    # if left:
        # print(str(n) + ' left')
    # else:
        # print(str(n) + ' right')
    # hanoi_tower_1(n-1, not left)


# 格雷码 Gray code

'''
the definition of Gray code
一个 n 位二进制的格雷码就是一个包含 2**n 种不同情况的列表，
每一种情况的 n 位二进制数与其上一种情况的 n 位二进制数正好有一位不同
n 位二进制的格雷码生成方式如下：
    1  n 位格雷码的 前 2**(n-1) 个代码字等于 n-1 位格雷码的代码字，按顺序书写，加前缀 0
    2  n 位格雷码的 后 2**(n-1) 个代码字等于 n-1 位格雷码的代码字，按逆序书写，加前缀 1
'''

# # using recursion to implement 使用递归实现,使用列表推导保存数据，输出格雷码

# def gray_code(n):                                   # 递归，代码简单，速度较应用序慢
    # if n == 1: return ['0','1']
    # return ['0'+i for i in gray_code(n-1)] + ['1'+i for i in gray_code(n-1)[::-1]]


# # for i in gray_code(5): print(i)

# # using for_loop to implement


# def gray_code_for(n):                                   # 最慢最菜的写法
    # list = [False for i in range(2**n)]
    # list[0] = '0'
    # list[1] = '1'
    # lst = list[:]
    # for i in range(2, n+1):
        # for j in range(2**(i-1)):
            # list[j] = '0'+lst[j]
            # list[j+2**(i-1)] = '1'+lst[:2**(i-1)][::-1][j]
        # lst = list[:]
    # return list


# def gray_code_for_2(n):                                 # 优化后的应用序实现，速度优势
    # list = ['0', '1']
    # for i in range(1,n):
        # left  = ['0'+i for i in list]
        # right = ['1'+i for i in list[::-1]]
        # list = left + right
    # return list

# import time


# def main(n):
    # a = time.perf_counter()
    # gray_code(n)
    # b = time.perf_counter()
    # gray_code_for(n)
    # c = time.perf_counter()
    # gray_code_for_2(n)
    # d = time.perf_counter()
    # print(b-a, c-b, d-c)        # 递归时间  垃圾时间  应用序时间


# if __name__ == '__main__':
    # main(10)    # >>> 0.001174527398641972  0.002195796209085674  0.0001979732319710389
    # main(17)    # >>> 0.23723541986879834   46.98887458702955     0.02618878659134083

####################################################################################

# 递归图形之 H 型树 

'''
基    例：当 n == 0 时什么也不画
归约条件：1. 绘制构成 H 型的三条线段
          2. 绘制4个 n-1 阶 H 树，分别连接到 H 的四个顶点（n-1 阶 H 树的大小是上一阶 n-2 阶 H 树的一半）
'''

# 调用 turtle 模块帮助可视化实现

# import turtle as t
# import random

# def set_screen():
    # t.setup(1000,800)
    # t.pu()
    # t.hideturtle()
    # t.pensize(3)
    # t.colormode(255)


# def draw_line(x1, y1, x2, y2):
    # t.pu()
    # t.goto(x1, y1)
    # t.pd()
    # t.goto(x2, y2)
    # t.pu()


# def draw_H(x, y, l):
    # line_a = [[x - l/2, y + l/2], [x - l/2, y - l/2]]
    # line_b = [[x - l/2, y], [x + l/2, y]]
    # line_c = [[x + l/2, y + l/2], [x + l/2, y - l/2]]
    # t.pencolor([random.randint(0,255) for i in range(3)])    # 随机画笔的颜色
    # draw_line(line_a[0][0], line_a[0][1], line_a[1][0], line_a[1][1])
    # draw_line(line_b[0][0], line_b[0][1], line_b[1][0], line_b[1][1])
    # draw_line(line_c[0][0], line_c[0][1], line_c[1][0], line_c[1][1])


# def tree_H(n, x, y, l):
    # if n == 0: return                       # 当 n == 0 时，什么也不画
    # draw_H(x,y,l)                           # 调用 draw_H 绘制一个 H 树
    # tree_H(n-1, x - l/2, y + l/2, l/2)      # 每一个 H 有四个顶点，所以有四个自身调用
    # tree_H(n-1, x - l/2, y - l/2, l/2)
    # tree_H(n-1, x + l/2, y + l/2, l/2)
    # tree_H(n-1, x + l/2, y - l/2, l/2)


# def main():
    # set_screen()
    # t.tracer(False)
    # tree_H(4, 0, 0, 300)
    # t.done()
    # t.tracer(True)


# if __name__ == '__main__': main()


############################################################################

# 动态编程技术，避免递归中的过度的重复计算

def fibonaci_dynamic(n):
    F = [False for i in range(n)]
    F[0] = 0
    F[1] = 1
    for i in range(2,n):
        F[i] = F[i-1] + F[i-2]
    return F[n-1]


def fibonaci_recursion(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonaci_recursion(n-1) + fibonaci_recursion(n-2)


# print(fibonaci_dynamic(101))    # 可以瞬间算出结果
# print(fibonaci_recursion(101))    # 会产生 RuntimeError:maximum recursion depth exceeded


# binary representation  二进制表示
'''
重复把 n 除以 2 ，然后反向读取所有的余数（即：辗转相除法）
编写一个 while 循环完成除以 2 的任务，并顺序输出各二进制，然后使用递归方法按正确顺序输出各二进制
'''

def decimal_to_binary_while_loop(n):
    s = ''
    while n > 0:
        s += str(n%2)
        n = n//2
    return s[::-1]


def decimal_to_binary_recursion(n, result = ''):
    if n == 0: return result
    return decimal_to_binary_recursion(n//2, str(n%2) + result)
    '''
    递归过程示例
    eg: decimal_to_binary_recursion(8, '')
            --> n == 8
            --> decimal_to_binary_recursion(4, '0') # 8//2, str(8%2) + ''
                --> n == 4
                --> decimal_to_binary_recursion(2, '00') # 4//2, str(4%2) + '0'
                    --> n == 2
                    --> decimal_to_binary_recursion(1, '000') # 8//2, str(2%2) + '00'
                        --> n == 1
                        --> decimal_to_binary_recursion(0, '1000') # 1//2, str(1%2) + '000'
                            --> n == 0
                            --> return '1000'    # result == '1000'
                        --> return '1000'    # decimal_to_binary_recursion(1, '000')
                    --> return '1000'    # decimal_to_binary_recursion(2, '00')
                --> return '1000'    # decimal_to_binary_recursion(4, '0')
            --> return '1000'    # decimal_to_binary_recursion(8, '')
    '''


# print(decimal_to_binary_recursion(166))     # >>> 10100110
# print(decimal_to_binary_while_loop(167))    # >>> 10100111


'A4 纸：基于 ISO 格式，纸张的宽高比为 pow(2, 0.5) 比 1，并定义 A0 纸的面积为 1 平方米'


# 全排列 permutation

'''

从n个不同元素中任取m（m≤n）个元素，按照一定的顺序排列起来，叫做从n个不同元素中取出m个元素的一个排列。
当m=n时所有的排列情况叫全排列。公式：全排列数f(n)=n!(定义0!=1)

# 给定的元素中，抽取一定数量的元素进行排列，求排列的总数
# 现以26个字母为例，从 a 开始，n 个字母的不同种排列数量为 n！ 将这 n！ 种不同排列进行输出  1 <= n <= 26
# eg: n == 3 时，输出为： bca cba cab acb bac abc
基本思路
    1. a    共 1 种情况(1!)
    2. ba --> ab  # 将 b 插入到已有元素 a 的前后位置    共 2 种情况(2!)
    3. cba cab --> bca bac acb abc  # 将 c 插入到已有元素 ba ab 的前面，中间，后面位置    共 6 种情况(3!)
'''

def factorial_recursion(n):
    if n <= 1: return 1
    return n * factorial_recursion(n-1)


# 递推实现全排列
def permutation_for_loop(n, letter):
    # 初始化一个列表，长度为排列的种数
    permutation_list = [0 for i in range(factorial_recursion(n))]
    # 创建临时列表，用于保存循环中元素的排列情况，初始化保存只有一个元素是的情况
    temporary_list = ['a']

    # 从 2 开始循环，因为只要一个元素的情况已保存
    for temp_x in range(2, n+1):
        # 计数，根据计数来更新列表 permutation_list 数据
        count = 0
        # for 循环遍历临时列表 temporary_list 获取每一个元素
        for temp_i in temporary_list:
            # for 循环遍历从列表 temporary_list 中取得的每一个元素的子元素
            for temp_j in temp_i:
                # 前缀插入，调用 str.replace() 方法返回一个新的字符串，并更新到 permutation_list 相应的位置，同时计数加 1
                permutation_list[count] = temp_i.replace(temp_j, letter[temp_x-1] + temp_j)
                count += 1
            # 完成后缀插入，计数加 1
            permutation_list[count] = temp_i + letter[temp_x-1]
            count += 1
        # 更新临时列表 permutation_list
        temporary_list = permutation_list[:factorial_recursion(temp_x)]

    # 返回结果
    return permutation_list


# 递归实现全排列
def permutation_recursion(n, letter):
    if n == 1: return [letter[n-1]]
    return [i.replace(j, letter[n-1]+j) for i in permutation_recursion(n-1, letter) for j in i] \
           + [i+letter[n-1] for i in permutation_recursion(n-1, letter)]


# # 调用函数
# letter = 'abcdefghijklmnopqrstuvwxyz'
# pr = permutation_recursion(4, letter)
# pr.sort()
# # 格式化打印
# for i in range(len(pr)):
    # print(pr[i], end = ' ' if (i+1)%4 != 0 else '\n')

# 调用函数
# pfl = permutation_for_loop(4, letter)
# pfl.sort()
# # 格式化打印
# for i in range(len(pfl)):
    # print(pfl[i], end = ' ' if (i+1)%4 != 0 else '\n')


# 列表的双层推导

# sentence ='I am lenrning Python now!'
# lst = [i for x in sentence for i in x]
# for i in lst:
    # print(i, end = '.')
# # >>> I. .a.m. .l.e.n.r.n.i.n.g. .P.y.t.h.o.n. .n.o.w.!.


'''排列 n 个元素中取出 k (k <= n) 个元素，组成一个排列，排列数量'''
# 重新定义了一个单独的函数实现 P(n, k) 的排列，输出 n 个元素中包含 k 个元素的所有排列
def permutation_k_recursion_1_count(n, k):
    if n == m: return 1
    return n * permutation_k_recursion_1_count(n-1, k-1)


# 依赖于已定义的阶乘函数 factorial_recursion() 来实现，根据 P(n, k) = n! / (n-k)!
def permutation_k_recursion_2_count(n, k):
    return factorial_recursion(n)//factorial_recursion(n-k)

# print(permutation_k_recursion_1_count(5, 4))
# print('###########################################')
# print(P(5, 4))


# 递推实现排列 P(n, k)， 完全不同于上面的全排列递归
def permutation_nk_recursion(n, k, letters, m = '', k_letter = ''):
    '''
    递推实现不同排列的输出
    参数：
        n --> 参与排列的元素的总数量 n <= len(letters)
        k --> 选取参与排列的元素的个数， k <= n
        letters --> 参与排列的元素选取的母本
        m --> 在函数调用中保存并固定初始的最初 n-k 作为递归结束的判断标记
        k_letter --> 保存参与排列的元素的列表
        ps: m, k_letter 在递归中能保证不变的原因：在最外层的函数调用过程获得值更新后，被保护起来，
                                                  在随后的递归过程中，都是在外层函数之内，所以也在 m 和 k_letter 的作用域内
    '''
    # 根据实际输入的 n, k, letters 值初始化 m, k_letter
    if m == '':
        m = n - k
        k_letter = list(letters[:n])
    # 递归基础
    if n == m+1: return k_letter
    # 初始化 num_of_perm，用于保存结果
    num_of_perm = []
    # 遍历上一级返回的结果列表中的元素，并与 perm 进行关联
    for perm in permutation_nk_recursion(n-1, k, letters, m, k_letter):
        # 'temp_letter 的逻辑：通过 for 循环遍历 k_letter， 如果遍历的元素不再perm中，则添加到 temp_letter 中'
        temp_letter = [i for i in k_letter if i not in perm]
        # 循环将 temp_letter 中的元素添加到 perm 的后面
        num_of_perm += [perm + i for i in temp_letter]
    # 返回结果
    return num_of_perm


# letters = 'abcdefghijklmnopqrstuvwxyz'
# p_nk_r = permutation_nk_recursion(5, 3, letters)
# p_nk_r.sort()
# for i in range(len(p_nk_r)):
    # print(p_nk_r[i], end = ' ' if (i+1)%12 != 0 else '\n')



def permutation_calculate(n, k):
    if n < k: return '错误，k 必须小于等于 n'
    if k == 0: return 1
    return n * permutation_calculate(n-1, k-1)


# print(permutation_calculate(4, 2))


# 书上的递归，感觉才是递归，自己写的总感觉没有脱离递推的思想
def perm_k(s, k):
    '''
    输出 s 个元素中选取 k 个元素组成的所有排列
    s --> string，为元素的母本
    k --> int，选取的元素的个数
    '''
    # 参数判断
    if k > len(s): return '参数错误'
    # recursive basis
    if k == 0: return ['']
    # recursive chain
    strings = []
    for i in range(len(s)):
        substrings = perm_k(s[:i]+s[i+1:], k-1)
        for substring in substrings:
            strings += [s[i] + substring]
    return strings


# print(perm_k('abcd', 2))



# 组合
# 1、全组合，n 个元素中选取元素进行组合，所有的组合的可能性
# 在排列的基础上进行修改就可以实现

def combination_all(s):
    '''
    本函数配合 combination_k 函数实现全组合
    s --> 组合元素的样本
    以列表的形式返回所有长度可能的组合
    
    测试如下：
    combination_all(s) >>> ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
    '''
    comb_list = []
    # 通过 for 循环调用 combination_k(s, k) 获取不同 k 值下的所有组合
    for i in range(1, len(s)+1):
        comb_list += combination_k(s, i)
    return comb_list


def combination_k(s, k):
    '''
    字符串 s 中选取 k(0 <= k <= len(s)) 个元素，进行组合，以列表的形式返回所有可能的组合
    s --> 输入的字符串
    k --> 选取的元素的个数
    
    测试结果如下：
    combination_k('abc', 2) >>> ['ab', 'ac', 'bc']
    
    combination_k('c', 2)   >>> []
        combination_k('c', 2) 的递归内部解释如下：
            --> combination_k('c', 2)
                --> for i in combination_k('', 1):
                        c + i
                    # 由于 combination_k('', 1) 的返回结果是一个空列表，这 for 循环遍历不会被执行，所以返回初始设定的值 []
    '''
    # recursive basis
    if k == 0: return ['']
    # recursive chain
    subletters = []
    # 此处涉及到一个 python 遍历循环的特点：当遍历的对象为空（列表，字符串...）时，循环不会被执行，range(0) 也是一样
    for i in range(len(s)):
        for letter in combination_k(s[i+1:], k-1):
            subletters += [s[i] + letter]
    return subletters


# def main():
    # letter = 'abcdefghijklmnopqrstuvwxyz'
    # print('组合及全组合计算器')
    # print('组合总样本：' + letter)
    # mode = eval(input('请选择运行模式：1 代表‘组合’； 2 代表‘全组合’:'))
    # if mode == 1:
        # print('您选择的是组合模式:')
        # length = eval(input('请输入组合元素样本的长度:'))
        # letter_numbers = eval(input('请输入入选组合元素的个数:'))
        # print('您选择的组合样本是：' + letter[:length] + ',参与组合的元素个数是：' + letter_numbers)
        # c_k = combination_k(letter[:length], letter_numbers)
        # print(c_k)
    # elif mode == 2:
        # print('您选择的是全组合模式:')
        # length = eval(input('请输入组合元素样本的长度:'))
        # print('您选择的组合样本是：' + letter[:length])
        # c_a = combination_all(letter[:length])
        # print(c_a)


# if __name__ == '__main__': main()


# 汉明距离 hanmming distance
'''
概念：两个长度相同的，长度为 n 的二进制字符串（简称位串）的汉明距离定义为两个位串之间不同位的个数
例如：
    位串 0000 ，汉明距离为 2 的所有位串为：
        0011  0101  0110  1010  1100
    观察上述位串，可以得出如下规律：
    1. 在 0000 的基础上，从最右端开始，选取两个位置的二进制字符进行反转，得到 0011
    2. 在 0011 的基础上，从右往左，最后一个 1 开始， 依次往右移动一位(两个位置进行调换)，可获得不同的汉明距离为 2 的位串
    
    以此规律，可获得递归的基础和链条，写出递归函数
'''


# 递推实现
def hamming_start(s, k, n=0):
    hamming_list = [s]
    while n+k < len(s):
        for i in range(k+n-1, n-1, -1):
            s = s[:i] + s[i+1] + s[i] + s [i+2:]
            hamming_list.append(s)
        n += 1
    return hamming_list


def hamming_distance(s, k):
    # 预处理，获取符合汉明距离为 k 的位串 s 的开始位串
    start = ''
    for i in range(len(s)):
        if i < k:
            if s[i] == '0':
                start += '1'
            else:
                start += '0'
        else:
            start += s[i]
    return hamming_start(start, k)


# 递归实现
def hamming_recursive(s, k):
    pass
    


# 反转字符，0 变 1，1 变 0
def flip(c):
    return str(1-int(c))


# 将字符串 s 中位置 i 的字符进行反转
def flip_s(s, i):
    t = s[:i] + flip(s[i]) + s[i+1:]
    return t


# 递归实现
def hamming(s, k):
    if k > 1:
        c = s[-1]
        # # s1 = [y+c for y in hamming(s[:-1], k)] if len(s) > k else []
        s1 = []
        if len(s) > k:
            for y in hamming(s[:-1], k):
                s1 += [y + c]
        else:
            s1 = []

        # s2 = [y+flip(c) for y in hamming(s[:-1], k-1)]
        s2 = []
        for y in hamming(s[:-1], k-1):
            s2 += [y + flip(c)]

        r = []
        r.extend(s1)
        r.extend(s2)
        return r
    else:
        return [flip_s(s, i) for i in range(len(s))]

# print(hamming("0000", 2))

# >>> ['1100', '1010', '0110', '1100', '1010', '0110']

# 递归跟踪示意
'''
hanming('0000', 2):
    2 > 1    # (True, k == 2)
        c = '0'    # ('0000'[-1] == '0')
        4 > 2      # (True, len('0000') == 4)
            s1 = [y + '0' for y in hamming('000', 2)]
                hamming('000', 2)
                    2 > 1    # (True, k == 2)
                        c = '0'     # ('000'[-1] == '0')
                        3 > 2       # (True, len('000') == 3)
                            s1 = [y + '0' for y in hamming('00', 2)]
                                hamming('00', 2)
                                    2 > 1    # (True, k == 2)
                                        c = '0'    # ('00'[-1] == '0')
                                        2 > 2      # (False, len('00') == 2)
                                            s1 = []
                                        s2 = [y + flip('0') for y in hamming('0', 1)]
                                            hamming('0', 1)
                                                1 > 1    # (False, k == 1)
                                                    ['1']    # ([flip_s('0', i) for i in range(len('0'))])
                                                return ['1']
                                            s2 = ['11']
                                        r.extend(s1), r.extend(s1)
                                        # (r = ['11'])
                                        return ['11'] 
                                s1 = ['110']
                        s2 = [y + flip('0') for y in hamming('00', 1)]
                            hanming('00', 1)
                                1 > 1 (False, k == 1)
                                ['10', '01']    # ([flip_s('00', i) for i in range(len('00'))])
                                return ['10', '01']
                            s2 = ['101', '011']
                        r.extend(s1), r.extend(s1)
                        # (r = ['110', '101', '011'])
                        return ['110', '101', '011'] 
                s1 = ['1100', '1010', '0110']
        s2 = [y + flip('0') for y in hamming('000', 1)]
            hamming('000', 1)
                1 > 1 (False, k == 1)
                ['100', '010', '001']    # ([flip_s('00', i) for i in range(len('00'))])
                return ['100', '010', '001']
            s2 = ['1100', '1010', '0110']
        r.extend(s1), r.extend(s1)
        # r = ['1100', '1010', '0110', '1100', '1010', '0110']
        return ['1100', '1010', '0110', '1100', '1010', '0110']
'''



# 二项分布 binomial distribution
'''
二项分布就是重复 n 次独立的伯努利试验
在每次试验中只有两种可能的结果，而且两种结果发生与否互相对立，并且相互独立，与其它各次试验结果无关，
事件发生与否的概率在每一次独立试验中都保持不变，
则这一系列试验总称为n重伯努利实验，当试验次数为1时，二项分布服从0-1分布。
'''

# 抛掷硬币 n 次，k 次正面朝上
def binomial(n, k):
    global count_11
    count_11 += 1
    if (n == 0) and (k == 0): return 1.0
    if (k > n) or (k < 0): return 0.0
    return (binomial(n-1, k) + binomial(n-1, k-1)) / 2.0


count_11 = 0

print(binomial(20, 10))
print(count_11)


def combination_calculate(n, k):
    return permutation_calculate(n, n) // (permutation_calculate(k, k) * permutation_calculate(n-k, n-k))


# 抛掷硬币 n 次，k 次正面朝上
# 记忆技术：以空间换时间，初始化一个符合要求的二维数组，根据内在的规律来更新列表的值 
def binomial_distribution(n, k):
    # 初始化二维列表 a ，大小为 (n+3) x (n+1)，填充元素为数字 0
    # 例如：抛掷2次，产生三种结果，正面朝上的次数分别是 0次，1次，2次
    # 在单行列表的首尾加上一个 0 赋予当 k > n 或者 k 
    a = [[0 for i in range(n+3)] for i in range(n+1)]
    a[0][1] = 1
    for i in range(1, n+1):
        for j in range(1, i+2):
            a[i][j] = (a[i-1][j] + a[i-1][j-1]) / 2.0
    return a[n][k+1]

print(binomial_distribution(2, 0))



def func_decorator_out(s):
    def func_decorator(f):
        def printf(*args):
            print(s)
            return f(*args)
        return printf
    return func_decorator


@ func_decorator_out(s = 'hello world')
def super_sum(*args):
    s_sum = 0
    for arg in args:
        s_sum += arg
    return s_sum



print(super_sum(1,2, 3, 4))


try:
    print(a)
except Exception:
    print('got an exception')
else:
    print('program is ok')
finally:
    print('test over')





## 变换 python 的工作目录
#   使用 os 模块即可实现
#  os.getcwd()        # 获取当前的操作目录
#  os.chdir('patch')  # 切换至指定目录















































































































