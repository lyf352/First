
#include <stdio.h>
int main ()
{
	int  bill = 0;
	int  price = 0;
	printf("请输入您的金额：");
	scanf("%d", &price);
	printf("请输入您的面值：");
	scanf("%d", &bill);
	if (bill <= price)
	{
		printf("您的金额不足以支付该面值！\n");
	}
	else
	{
		printf("您支付的金额为：%d\n", bill);
		printf("您需要找零的金额为：%d\n", bill - price);
	}
 }