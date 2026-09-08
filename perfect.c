#include<stdio.h>
int main(){
    int num,a,b=0;
    printf("Enter a number:");
    scanf("%d",&num);
    for(int i=1;i<num;i++){
        a=num%i;
        if(a==0){
            
            b=b+i;
            
        }
        
    }
    if(b==num)
    printf("Perfect number");
    else
    printf("Not a perfect number");
    return 0;
        
    }


