// 3
// 9 8 7 
// 6 5 4 
// 3 2 1 

#include<iostream>
using namespace std;

int main(){

    int n, i = 1;
    cin >> n;
    int toPrint = n*n;
    
    while (i<=n)
    {
        int j = 1;
        while (j<=n)
        {
            cout << toPrint << " ";
            toPrint--;
            j++;
        }
        cout << endl;
        i++;
    }
    return 0;
}