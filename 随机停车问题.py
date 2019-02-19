# 随机停车

# 问题简化：现有长度为 10 的马路，停车所需的长度为 1，车辆随机停放（只要能放下），那么平均额可以停几辆车
# 蒙特卡罗法进行模拟100次，使用递归解决一次的辆数

import random

count = 0
def parking(low, hight, car):
    
    if hight - low < car:
        return 0
    else:
        n = random.uniform(low, hight - car)
        return parking(low, n, car) + 1 +  parking(n + car, hight, car)
sum = 0

for i in range(10000):
    sum += parking(0, 5, 1)
    
print(sum/10000)