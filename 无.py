import random

choices = ['石头', '剪刀', '布']
win_rule = {'石头': '剪刀', '剪刀': '布', '布': '石头'}

while True:
    user = input('请输入 石头/剪刀/布 (q退出): ')
    if user == 'q':
        break
    if user not in choices:
        print('输入无效，请重新输入')
        continue

    computer = random.choice(choices)
    print(f'电脑出了: {computer}')

    if user == computer:
        print('平局')
    elif win_rule[user] == computer:
        print('你赢了！')
    else:
        print('你输了！')