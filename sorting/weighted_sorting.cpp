// weighted sorting
#include <bits/stdc++.h>
#include<cmath>
#include<map>
#include<typeinfo>
#include <string>
using namespace std;

void sort(map<int, int>& M)
{

    multimap<int, int> MM;

    for (auto& it : M) {
        MM.insert({ it.second, it.first });
    }
 
    for (auto& it : MM) {
        cout << it.second << ' ' << it.first << endl;
    }
}

int main() {
    int arr[5]={10, 36, 54,89,12};
    int weight[5]={0,0,0,0,0};
    map<int,int> final;
    for(int i=0; i<5; i++){
        if(ceil((double)sqrt(arr[i])) == floor((double)sqrt(arr[i]))){
            weight[i]+=5;
        }
        if(arr[i]%4==0 && arr[i]%6==0){
            weight[i]+=4;
        }
        if(arr[i]%2==0){
            weight[i]+=3;
        }
        else{
            weight[i]=0;
        }
        final[arr[i]]=weight[i];
    };
    sort(final);
    return 0;
}
