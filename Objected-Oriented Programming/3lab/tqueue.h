#ifndef LAB_3_TQUEUE_H
#define LAB_3_TQUEUE_H

#include "tqueueitem.h"

class TQueue {
public:
    TQueue();
    TQueue(const TQueue &other) = default;
    ~TQueue();

    friend ostream &operator<<(ostream &os, const TQueue &q);
    bool push(shared_ptr<Triangle> &&triangle);
    bool pop();
    shared_ptr<Triangle> top();
    bool empty();
    size_t size();

private:
    shared_ptr<TQueue_item> first;
    shared_ptr<TQueue_item> last;
    size_t n;
};


#endif //LAB_3_TQUEUE_H