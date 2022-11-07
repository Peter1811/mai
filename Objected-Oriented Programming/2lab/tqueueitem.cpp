#include "tqueueitem.h"

TQueue_item::TQueue_item(const Triangle &triangle) {
  this->triangle = triangle;
  this->next = nullptr;
  cout << "Queue item: created" << endl;
}

TQueue_item::TQueue_item(const TQueue_item &other) {
  this->triangle = other.triangle;
  this->next = other.next;
  cout << "Stack item: copied" << endl;
}

TQueue_item *TQueue_item::SetNext(TQueue_item *next_) {
  TQueue_item *prev = this->next;
  this->next = next_;
  return prev;
}

Triangle TQueue_item::GetTriangle() { return this->triangle; }

TQueue_item *TQueue_item::GetNext() { return this->next; }

TQueue_item::~TQueue_item() {
  cout << "Queue item: deleted" << endl;
  delete next;
}

ostream &operator<<(ostream &os,
                    const TQueue_item &obj) { // перегруженный оператор вывода
  os << "{";
  os << obj.triangle;
  os << "}" << endl;
  return os;
}