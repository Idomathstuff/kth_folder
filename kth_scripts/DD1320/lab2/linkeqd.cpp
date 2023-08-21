// C++ program for the above approach

#include <bits/stdc++.h>
using namespace std;

struct QNode
{
    int data;
    QNode *next;
    QNode(int d) // __init__
    {
        data = d;
        next = NULL; // memory of *next is null
    }
};

struct Queue
{
    QNode *front; // Theyre pointers which means they can act as a struct but also memory can be swapped out with other QNodes
    QNode *rear;
    int length = 0;
    Queue(){
        front = rear = NULL;} // __init__

    void enQueue(int x){
        QNode *temp = new QNode(x); // QNode(x) being put memory of *temp
        if (rear == NULL)
        {
            front = rear = temp;
            return;
        }
        rear->next = temp; // because *next is a pointer you can store memory in next
        rear = temp;
        length+=1;
    }


    void deQueue(){
        if (front == NULL)
            return;
        QNode *temp = front;
        front = front->next; // memory of *next is stored in memory of *front
        if (front == NULL)
            rear = NULL;
        delete (temp);
        length -=1;

    }

    void print()
    {
        for (int i=0; i<length-1;i++){
            QNode *temp;

        }        
    }
};

struct Kue
{
    QNode k;
    void enqueue(int x)
    {

    }
}; 

int main()
{
    Queue q;
    q.enQueue(10);
    q.enQueue(20);
    // q.deQueue();
    // q.deQueue();
    q.enQueue(30);
    q.enQueue(40);
    // q.enQueue(50);
    // q.deQueue();
    QNode *k = new QNode(2);
    k->next = new QNode(3);
    k->next->next = new QNode(4);
    k->next->next->next = new QNode(5);
    cout << k->next->data;
    cout << k->next->next->data;
    cout << k->next->next->next->data;
    // cout << (q.front);

    // cout << "Queue Front : " << ((q.front != NULL) ? (q.front)->data : -1) << endl;
    // cout << "Queue Rear : " << ((q.rear != NULL) ? (q.rear)->data : -1);
    return 0;
}
