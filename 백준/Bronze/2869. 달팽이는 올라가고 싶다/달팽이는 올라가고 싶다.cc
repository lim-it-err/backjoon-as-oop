#include <stdio.h>
int main()
{
	int cnt,A,B,V;
	scanf("%d",&A);
	scanf("%d",&B);
	scanf("%d",&V);
	
	cnt=(V-A)/(A-B);
	if((V-A)%(A-B)==0) cnt++;
	else cnt=cnt+2;
	printf("%d",cnt);
}