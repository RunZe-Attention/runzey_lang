//
// Created by 杨润泽 on 2022/4/6.
//



#include<iostream>
using  namespace  std;
const int size=10;
template<class T>                     //模板声明，其中T为类型参数
class Stack{                          //类模板为Stack
public:
    void init()
    {
        tos=0;
    }
    void push(T ob);                    //声明成员函数push的原型，函数参数类型为T类型
    T pop();                            //声明成员函数pop的原型，其返回值类型为T类型
private:
    T stack[size];                      //数组类型为T，即是自可取任意类型
    int tos;
};

template<class T>                     //模板声明
void Stack<T>::push(T ob)             //在类模板体外定义成员函数push
{
    if(tos==size)
    {
        cout<<"Stack is full"<<endl;
        return;
    }
    stack[tos]=ob;
    tos++;
}
template<typename T>                  //模板声明
T Stack<T>::pop()                               //在类模板体外定义成员函数push
{
    if(tos==0)
    {
        cout<<"Stack is empty"<<endl;
        return 0;
    }
    tos--;
    return stack[tos];
}
