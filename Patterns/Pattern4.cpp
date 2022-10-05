// 3
// 1 2 3 
// 4 5 6 
// 7 8 9 

#include<iostream>
using namespace std;

int main(){

    int n, i = 1, toPrint = 1;
    cin >> n;
    
    while (i<=n)
    {
        int j = 1;
        while (j<=n)
        {
            cout << toPrint << " ";
            toPrint++;
            j++;
        }
        cout << endl;
        i++;
    }
    return 0;
}