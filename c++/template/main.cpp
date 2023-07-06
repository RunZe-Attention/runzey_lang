#include <iostream>
#include "stack.hpp"


using namespace  std;

template<typename T>    //模板声明，其中T为类型参数
class Compare{
  public:
   Compare(T i,T j)
   {
    x = i;
    y = j;
   }
   T max()
   {
    return (x>y)?x:y;
   }
  private:
   T x,y;
};


template<typename T>
class Add{
public:
    Add(T a,T b)
    {
        x = a;
        y = b;
    }
    T add()
    {
        return x + y;
    }
private:
    T x;
    T y;
};

template<typename T>
class subtraction{
public:
    subtraction(T a,T b)
    {
        x=a;
        y=b;
    }
    T Sub();
private:
    T x;
    T y;

};
template<typename T>
T subtraction<T>::Sub()
{
    return x-y;
}


template<typename T1,typename T2>
class Myclass{
public:
    Myclass(T1 a, T2 b);
    void show();

private:
    T1 x;
    T2 y;
};

template<typename T1,typename T2>
Myclass<T1,T2>::Myclass(T1 a, T2 b)
{
    x=a;
    y=b;
}
template<typename T1,typename T2>
void Myclass<T1,T2>::show()
{
    cout<<x<<endl;
    cout<<y<<endl;
}



template<typename T>
class Mul{
public:
    Mul(T a,T b)
    {
       x = a;
       y = b;
    }
    T cheng();
private:
    T x;
    T y;
};
template<typename T>
T Mul<T>::cheng() {
    return x * y;
}



int main() {
    Compare<int> com1(3, 7);
    Compare<double> com2(12.34, 56.78);
    Compare<char> com3('a', 'x');
    cout << "其中的最大值是:" << com1.max() << endl;
    cout << "其中的最大值是:" << com2.max() << endl;
    cout << "其中的最大值是:" << com3.max() << endl;
    Add<int>add1(10,20);
    cout << "和是:" << add1.add() << endl;

    subtraction<int> sub1(6,2)  ;
    cout << "sub is:" << sub1.Sub()<<endl;

    Stack<char> s1;
    s1.init();
            s1.push('a');
            s1.push('b');
            s1.push('c');
    
    for(int i ; i < 3; ++i)
    {

         cout<<s1.pop()<<endl;

    }
    

    Stack<int>s2;
    s2.init();
    s2.push(1);
    s2.push(2);
    s2.push(3);
    for(int i = 0 ;i<3;++i)
    {
        cout<<s2.pop()<<endl;
    }


    Myclass<int ,string>m1(10000,"afafj");
    m1.show();

    Mul<int>mu1(3,4);
    cout<<mu1.cheng()<<endl;

    return 0;
}