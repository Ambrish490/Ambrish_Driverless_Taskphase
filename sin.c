#include<stdio.h>
#include<math.h>
int main(){
    float a,b=0.0,x,c,s=0.0;
    int n,k;
    printf("Enter Angle:");
    scanf("%f",&x);
    printf("Enter Number of terms");
    scanf("%d",&n);
    a=3.14159265;
    c=x*(a/180.0);
    
    for(int i=1;i<=n;i++){
    k=1;
    
     for(int j=1;j<=(i*2-1);j++){
        k=k*j;


     }
     s=s+pow(-1,(i+1))*(pow(c,(i*2-1))/k);

    }
    printf("%f",s);
    return 0;
    

}