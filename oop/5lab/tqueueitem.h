
#ifndef INC_4_LAB_QUQUE_ITEM_H
#define INC_4_LAB_QUQUE_ITEM_H

#include "triangle.h"
#include <memory>

using namespace std;

template <typename T> class TQueue_item {
public:
  TQueue_item() = default;
  TQueue_item(const shared_ptr<T> &item);
  TQueue_item(const shared_ptr<TQueue_item<T>> &other);
  ~TQueue_item() = default;

  shared_ptr<TQueue_item<T>> SetNext(shared_ptr<TQueue_item<T>> &next_);
  shared_ptr<TQueue_item<T>> GetNext();
  shared_ptr<T> GetItem();

  template <typename A>
  friend ostream &operator<<(ostream &os, const TQueue_item<A> &obj);

private:
  shared_ptr<T> item;
  shared_ptr<TQueue_item<T>> next;
};
#include "tqueueitem.inl"
#endif // INC_4_LAB_QUQUE_ITEM_H
