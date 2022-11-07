#ifndef INC_2_LAB_QUQUE_ITEM_H
#define INC_2_LAB_QUQUE_ITEM_H

#include "triangle.h"

class TQueue_item {
public:
    TQueue_item(const Triangle &triangle);

  TQueue_item(const TQueue_item &other);

  TQueue_item *
  SetNext(TQueue_item *next_); // присваивает значение следующему элементу

  TQueue_item *GetNext(); // возвращает указатель на следующий элемент

  Triangle GetTriangle();

  friend ostream &operator<<(ostream &os, const TQueue_item &obj);

  virtual ~TQueue_item();

private:
  Triangle triangle;
  TQueue_item *next;
};

#endif // INC_2_LAB_QUQUE_ITEM_H
