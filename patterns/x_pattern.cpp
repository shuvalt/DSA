// x pattern for odd length string
#include <iostream>
#include <string>
using namespace std;
int main() {
    
    string name;
    cin >> name;
    int n = name.length();
    
    for (int i = 0; i <= n; i++) { 
        for (int j = 0; j <= n; j++) { 
            if (j == i) 
                cout << name[i]; 
            else if(j == n-i-1)
                cout << name[j];
            else
                cout << " "; 
        }
        cout << endl;
}
}
