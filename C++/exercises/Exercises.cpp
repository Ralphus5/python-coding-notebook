#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void other() {
    int number = 0;
    cout << "hey" << endl;          // cannot use ' for strings
}

int other2() {
    int number = -255;
    cout << number << endl;
    return 0;
}

int other3() {
    int number = 100;
    int another = number;
    cout << another << endl;
    return 0;
}

int other4() {
    srand(time(0)); // seconds passed since jan 1st 1970
    int number = rand() % 10;
    cout << number;
    return 0;
}

int main() {
    double price = 99.99;
    float interestRate = 3.67F;
    long fileSize = 90000L;
    char letter = 'a';
    bool isValid = false;
    auto WhatisThis = true;  // auto assigns the variable type automatically
    double number = {1.2};   // do not use auto here, outherwise it cannot be printed
    cout << number << endl;
    other();
    other2();
    other3();
    other4();
    return 0;
}

