#include <bits/stdc++.h>
#include <iostream>
using namespace std;

struct QNode
{
    int data;
    QNode *next; //structure member variable that makes Qnode object pointer under name next 
    QNode(int d) // actions performed when object is created
    {
        data = d; // when the object is called, self.data becomes d
        next = NULL; // next is a Qnode, the memory isn't stored and is instead NULL
    }
};


struct Queue
{
    QNode *front; // front is memory to *front
    QNode *rear;

    Queue()
    {
        front = rear = NULL; // memory of NULL
    }
    void enQueue(int x)
    {
        QNode *temp = new QNode(x);
        if (rear == NULL)
        {
            front = rear = temp;
            return;
        }
        rear->next=temp;
        rear = temp;
    }
    void deQueue()
    {
        if (front==NULL)
            return;
        QNode *temp = front;
        front = front->next;
        if (front==NULL)
            rear = NULL;
        delete(temp);
    }
};



// struct foo
// {
//     int bar1=16;
// };

// ostream &operator<<(ostream &os, const foo &obj)
// {
//     os << obj.bar1;
//     return os;
// }

// void print(int arr[], int size)
// {
//     int size = sizeof(arr) / sizeof(arr[0]);
//     printf("[");
//     for (int i = 0; i < size; i++)
//     {
//         printf("%d", arr[i]);
//         if (i < size - 1)
//         {
//             printf(", ");
//         }
//     }
//     printf("]\n");
// }

int main()
{
    int a = 2;
    int *b;
    b = &a;
    cout << b;
    cout <<"\n" << &a;
    return 0;
}