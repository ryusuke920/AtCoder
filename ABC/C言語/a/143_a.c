#include<stdio.h>
int main(void){
int A, B, sum;
scanf("%d%d",&A,&B);
if(A>=2*B){
sum=A-2*B;
printf("%d",sum);
}else{
    printf("0");
}
return 0;
}