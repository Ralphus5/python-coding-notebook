#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    const short minValue = 1;
    const short maxValue = 6;

    srand(time(0));
    short dice1 = (rand() % maxValue) + minValue;
    short dice2 = (rand() % maxValue) + minValue;
    cout << dice1 << endl << dice2;
    return 0;
}