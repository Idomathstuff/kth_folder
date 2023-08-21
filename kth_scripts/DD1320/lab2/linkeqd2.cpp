// C++ program for the above approach

#include <bits/stdc++.h>
using namespace std;



struct QNode
{
    int data;
    QNode *next;

};

int main()
{
    QNode k;
    k.data = 1;
    k.next->data = 2;
    k.next->next->data = 3;
    k.next->next->next->data = 4;
    return 0;
}
