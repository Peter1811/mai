#ifndef INC_2_LAB_TQUEUE_H
#define INC_2_LAB_TQUEUE_H

#include "tqueueitem.h"

class TQueue {
public:
  TQueue();

  TQueue(const TQueue &other);

  ~TQueue();

  friend ostream &operator<<(ostream &os, const TQueue &q);

  bool push(Triangle &&Triangle);

  bool pop();

  Triangle top();

  bool empty();

  size_t size();

  void Clear();
private:
  TQueue_item *first;
  TQueue_item *last;
  size_t n;
};

#endif // INC_2_LAB_TQUEUE_H
