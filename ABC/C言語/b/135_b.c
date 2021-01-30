#include<stdio.h>
int main(void){
int N, ch=0;
scanf("%d",&N);
int P[100];
for(int i=0;i<N;i++){
    scanf("%d",&P[i]);
}
for(int i=1;i<=N;i++){
    if(i==P[i-1]) ch++;
}
if(ch==N-2 ||ch==N)printf("YES\n");
else printf("NO\n");
return 0;
}