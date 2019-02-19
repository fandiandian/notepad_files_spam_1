# 汉诺塔(hanoi tower) 递归实现

'''
递归实现原理：
设有 A, B, C 三个柱子，初始情况是： A 柱上有 n 个盘子，先需将这个 n 个盘子通过 B 柱全部移动到 C 柱上
递归链条
    1 将 n - 1 个盘子通过 C 柱移动道 B 柱上，再将 A 柱上的第 n 个盘子移动到 C 柱上；
    2 将 B 柱上的 n - 1 盘子通过 A 柱全部移动到 C 柱上，完成所有的移动
递归基例
    当 n = 1 时，直接将 A 柱上的盘子移动到 C 柱上，完成移动
'''

def hanoi_tower(n, A, B, C):
    global count
    if n == 1:
        print('将第 {} 块圆盘从 {} 柱移动到 {} 柱'.format(n, A, C))
        count += 1
    else:
        hanoi_tower(n - 1, A, C, B)
        count += 1
        print('将第 {} 块圆盘从 {} 柱移动到 {} 柱'.format(n, A, C))
        hanoi_tower(n - 1, B, A, C)

count = 0
hanoi_tower(4, '左', '中', '右')
print(count)