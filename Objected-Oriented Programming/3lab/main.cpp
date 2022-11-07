#include <iostream>
#include "tqueue.h"

using namespace std;

int main() {

    TQueue queue;
    vector <Point> v {Point(0, 1), Point(0,0), Point(1,1)};
    queue.push(make_shared <Triangle>(Triangle(v)));
    queue.push(make_shared <Triangle>(Triangle()));
    cout << queue;

    return 0;
}