

#include "tqueueitem.h"
#include <iostream>

using namespace std;

template <class T> TQueue_item<T>::TQueue_item(const shared_ptr<T> &rectangle) {
  this->item = rectangle;
  this->next = nullptr;
  cout << "Queue item: created" << endl;
}

template <class T>
TQueue_item<T>::TQueue_item(const shared_ptr<TQueue_item<T>> &other) {
  this->item = other->item;
  this->next = other->next;
  cout << "Queue item: copied" << endl;
}

template <class T>
shared_ptr<TQueue_item<T>>
TQueue_item<T>::SetNext(shared_ptr<TQueue_item<T>> &next_) {
  shared_ptr<TQueue_item<T>> prev = this->next;
  this->next = next_;
  return prev;
}

template <class T> shared_ptr<T> TQueue_item<T>::GetItem() {
  return this->item;
}

template <class T> shared_ptr<TQueue_item<T>> TQueue_item<T>::GetNext() {
  return this->next;
}

template <class T>
ostream &
operator<<(ostream &os,
           const TQueue_item<T> &obj) { // перегруженный оператор вывода
  if (obj.item) {
    os << "{";
    os << *(obj.item);
    os << "}" << endl;
  }
  return os;
}