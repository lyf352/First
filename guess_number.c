#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int answer, guess, count = 0;

    printf("==============================\n");
    printf("       猜数字游戏\n");
    printf("==============================\n");
    printf("我已经想好了一个 1 到 100 之间的数字\n");
    printf("看看你几次能猜中！\n");
    printf("------------------------------\n");

    srand((unsigned int)time(NULL));
    answer = rand() % 100 + 1;

    while (1) {
        printf("请输入你猜的数字：");
        scanf("%d", &guess);
        count++;

        if (guess < 1 || guess > 100) {
            printf("请输入 1 到 100 之间的数字！\n");
        } else if (guess < answer) {
            printf("太小了，再大一点！\n");
        } else if (guess > answer) {
            printf("太大了，再小一点！\n");
        } else {
            printf("------------------------------\n");
            printf("恭喜你，猜对了！答案就是 %d\n", answer);
            printf("你一共猜了 %d 次\n", count);
            printf("==============================\n");
            break;
        }
    }

    return 0;
}
