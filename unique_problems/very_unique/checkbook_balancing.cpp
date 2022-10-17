#include <iostream>

#include <cstdlib>

#include <cctype>

#include "checkbook.cpp"

using namespace std;

class checkbook

{

private:

float balance;

public:

void initbalance(float x);

void writecheck(float x);

void makedeposit( float x);

float getbalance() const;

};

//Here is the class definition, checkbook.cpp.

void checkbook::initbalance(float x)

{

if (x >=0)

balance = x;

else

cout <<"Invalid initialization "<<x<<endl;

}

void checkbook::writecheck(float x)

{

if (x > balance)

cout << "Insufficient funds -- current balance is"<<balance<<endl;

else

balance -=x;

}

void checkbook::makedeposit(float x)

{

if (x > 0)

balance += x;

else

cout <<"Invalid Deposit "<<x<<endl;

}

float checkbook::getbalance()const

{

return balance;

}

//Here's a little program which uses the class

int main()

{

    

checkbook mycheckbook; // mycheckbook is an object; checkbook isa class

mycheckbook.initbalance(500.00); // start with a balance of$500

mycheckbook.writecheck(50.0); // write a check for $50

mycheckbook.writecheck(345.76); // write a check for $345.76

mycheckbook.makedeposit(300.0); // deposit $300

cout<<"current balance : $"<<mycheckbook.getbalance()<<endl;

return 0;

}