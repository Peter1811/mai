#include "tqueue.h"

TQueue::TQueue() : first(nullptr), last(nullptr), n(0) {}

ostream &operator<<(ostream &os, const TQueue &q) {
  shared_ptr<TQueue_item> item = q.first;
  while (item) {
    os << *item;
    item = item->GetNext();
  }
  return os;
}

bool TQueue::push(shared_ptr<Triangle> &&triangle) {
  shared_ptr<TQueue_item> tail =
      make_shared<TQueue_item>(TQueue_item(triangle));
  if (tail == nullptr) {
    return false;
  }
  if (this->empty()) { // если пустая очередь, то голова и хвост - один и тот же
                       // элемент
    this->first = this->last = tail;
  } else if (n == 1) { // хвост - вставляемый элемент, а также следующий элемент
                       // от первого
    last = tail;
    first->SetNext(tail);
  } else {
    this->last->SetNext(tail); // хвост - следующий элемент от последнего
    last = tail;
  }
  n++;
  return true;
}

bool TQueue::pop() {
  if (first) {
    first = first->GetNext();
    return true;
  }
  return false;
}

shared_ptr<Triangle> TQueue::top() {
  if (first) {
    return first->GetTriangle();
  }
}

size_t TQueue::size() { return n; }

bool TQueue::empty() { return first == nullptr; }

TQueue::~TQueue() {}