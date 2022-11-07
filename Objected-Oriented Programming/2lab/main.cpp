#include "tqueue.h"
#include <iostream>

using namespace std;

int main() {
  auto *q = new TQueue;
  vector<Point> v{Point(0, 0), Point(0, 1), Point(1, 1)};
  /*Triangle r(v);
  ++r;
  Triangle r1;
  cin >> r1;
  Triangle r2 = r1 + r;
  TQueue_item q1(r1);
  cout << q1 << endl; */
  cout << Triangle(v).Area() << endl;
  q->push(Triangle(v));
  q->push(Triangle());
  cout << *q << endl;
  q->Clear();
  cout << q->size() << endl;
  return 0;
}
