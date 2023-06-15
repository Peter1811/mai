#include "triangle.h"
#include "tqueue.h"
#include <iostream>

using namespace std;

int main() {
  vector<Point> v{Point(0, 0), Point(0, 1), Point(1, 1)};
  {
    TQueue_item<Triangle> item(make_shared<Triangle>(v));
    cout << item;
  }
  TQueue<Triangle> queue;
  queue.push(make_shared<Triangle>(v));
  queue.push(make_shared<Triangle>());
  cout << queue;
  return 0;
}
