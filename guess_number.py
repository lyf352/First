import random

def guess_number():
    print("=" * 30)
    print("    猜数字游戏")
    print("=" * 30)
    print("我已经想好了一个 1 到 100 之间的数字")
    print("看看你几次能猜中！")
    print("-" * 30)

    answer = random.randint(1, 100)
    count = 0

    while True:
        try:
            guess = int(input("请输入你猜的数字："))
            count += 1

            if guess < 1 or guess > 100:
                print("请输入 1 到 100 之间的数字！")
            elif guess < answer:
                print("太小了，再大一点！")
            elif guess > answer:
                print("太大了，再小一点！")
            else:
                print("-" * 30)
                print(f"恭喜你，猜对了！答案就是 {answer}")
                print(f"你一共猜了 {count} 次")
                print("=" * 30)
                break
        except ValueError:
            print("请输入有效的整数！")

if __name__ == "__main__":
    guess_number()
