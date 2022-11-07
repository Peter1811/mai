
#ifndef INC_4_LAB_TQUEUE_H
#define INC_4_LAB_TQUEUE_H

#include "tqueueitem.h"

using namespace std;

template <class T> class TQueue {
public:
  TQueue();

  TQueue(const TQueue<T> &other);

  ~TQueue() = default;

  template <class A>
  friend ostream &operator<<(ostream &os, const TQueue<A> &q);

  bool push(shared_ptr<T> &&item);

  bool pop();

  shared_ptr<T> top();

  bool empty();

  size_t size();

private:
  shared_ptr<TQueue_item<T>> first;
  shared_ptr<TQueue_item<T>> last;
  size_t n;
};
#include "tqueue.inl"

#endif // INC_4_LAB_TQUEUE_H
