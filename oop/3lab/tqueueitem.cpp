#include "tqueueitem.h"

TQueue_item::TQueue_item(const shared_ptr<Triangle> &triangle) {
  this->triangle = triangle;
  this->next = nullptr;
  cout << "Queue item: created" << endl;
}

TQueue_item::TQueue_item(const shared_ptr<TQueue_item> &other) {
  this->triangle = other->triangle;
  this->next = other->next;
  cout << "Queue item: copied" << endl;
}

shared_ptr<TQueue_item> TQueue_item::SetNext(shared_ptr<TQueue_item> &next_) {
  shared_ptr<TQueue_item> prev = this->next;
  this->next = next_;
  return prev;
}

shared_ptr<Triangle> TQueue_item::GetTriangle() { return this->triangle; }

shared_ptr<TQueue_item> TQueue_item::GetNext() { return this->next; }

TQueue_item::~TQueue_item() { cout << "Queue item: deleted" << endl; }

ostream &operator<<(ostream &os,
                    const TQueue_item &obj) { // перегруженный оператор вывода
  os << "{";
  os << *(obj.triangle);
  os << "}" << endl;
  return os;
}