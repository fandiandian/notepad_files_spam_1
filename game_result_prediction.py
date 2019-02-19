# 自顶向下分析，自底向上编程
# 体育竞技结果预测
'''
以乒乓球为例，给定两位选手的能力值，通过产生随机数，获得单回合比赛的结果，单局比赛先获得15分的选手得1分
比赛执行n个局，最终可以模拟比赛的结果
'''

'''
自顶向下分析：
设定主函数: main()，需要实现的效果：
    1、printinfo() 向用户展示该程序的作用
    2、getinput() 获取相应的数据
    3、sim_n_game() 模拟比赛 n 局
    4、printsummary() 输出比赛结果

其中 sim_n_game 向下分析：模拟单局比赛的结果 sim_one_game()
    单局比赛中包含单局比赛的终止条件：gameover(); 胜局分的比较函数 mmax()

自底向上编程
根据分析的结果，从底部向上编程，逐步完成主函数的各个组件
次序如下：
    printinfo() --> getinput() --> gameover() --> mmax() --> sim_one_game() --> sim_n_game() --> printsummary() --> main()
'''

import random

def printinfo() :
    print('*_'*20 + '*')
    print('')
    print('')
    match_rules = '''说明如下：
    1、这是一个预测双人的竞技比赛胜率的程序，需要您提供比赛双方的能力值，以及比赛的局数
    2、运动员的能力值(整数)，范围是：1 ~ 100
    3、第一回合发球方随机，随后的回合胜者发球，单回合比赛胜利者得回合分1分；
    4、一局比赛为29回合，先得15分者，胜利，得胜局分1分
    5、模拟比赛进行规定的局数，对结果进行分析'''
    print(match_rules)
    print('程序开始......\n')

def getinput() :
    player_A = eval(input('请输入第一位选手的能力值：\n'))
    player_B = eval(input('请输入第二位选手的能力值：\n'))
    number_of_games = eval(input('请输入比赛的局数\n'))
    print('*_'*8 + ' 比赛开始 ' + '_*'*8)
    return player_A, player_B, number_of_games

def gameover(rounds = 29) :
    round_A = round_B = rounds//2 + 1
    return round_A, round_B

def mmax(a, b) :
    return a if a > b else b

def sim_one_game(player_A, player_B) :
    max_round = round_A = round_B = 0
    starting = 'a' if random.randint(0,1) == 0 else 'b'
    while max_round not in gameover() :
        if starting == 'a' :
            if random.randint(1, player_A + player_B) <= player_A :
                round_A += 1
            else :
                round_B += 1
                starting = 'b'
        else :
            if random.randint(1, player_A + player_B) > player_A :
                round_B += 1
            else :
                round_A += 1
                starting = 'a'
        max_round = mmax(round_A, round_B)
    return 'win_A' if round_A > round_B else 'win_B'

def sim_n_game(player_A, player_B, number_of_games) :
    win_A = win_B = 0
    for i in range(number_of_games):
        wins = sim_one_game(player_A, player_B)
        if wins == 'win_A' :
            win_A += 1
        else :
            win_B += 1
    return win_A, win_B

def printsummary(win_A, win_B, number_of_games) :
    print('比赛结果如下：')
    print('双方选手进行了 {:^5} 局比赛'.format(number_of_games))
    print('第一位选手的胜场数是：{:^6}，胜率是：{:^6.2%}'.format(win_A, win_A/number_of_games))
    print('第二位选手的胜场数是：{:^6}，胜率是：{:^6.2%}'.format(win_B, win_B/number_of_games))

def main() :
    printinfo()
    g_input = getinput()
    s_n_game = sim_n_game(g_input[0], g_input[1], g_input[2])
    printsummary(s_n_game[0], s_n_game[1], g_input[2])

main()























